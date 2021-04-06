from custom_zipfile import ZipFile, BadZipFile
import os
import chardet # pip install
import re
import argparse
from pyads import ADS

class check_source:
    def __init__(self, path):
        self.path = path
        self.LFH = dict()
        self.detector = chardet.UniversalDetector()
        self.zip = ZipFile(self.path)
        self.filelist = ZipFile.infolist(self.zip)
        self.result = list()
        self.korean_file = ''

    def stored_header(self):
        for file in self.filelist:
            self.zip.open(file.filename)
            self.Local_Header(self.zip.min_lfh)

    def Local_Header(self, file):
        self.LFH[file["filename"]] = file

    def created_env(self):
        # access_time = os.path.getatime(self.path)
        create_time = os.path.getctime(self.path)
        modified_time = os.path.getmtime(self.path)
        if create_time <= modified_time:  # local or download
            handler = ADS(self.path)
            if handler.has_streams():  # download
                for stream in handler:
                    rtn = handler.get_stream_content(stream)
                    if b'ZoneId=3' in rtn:
                        self.result.append("Not_time_reversal")
                        self.result.append("download")
                    else:
                        self.result.append("Unknown")
            else:  # local
                self.result.append("Not_time_reversal")
                self.result.append("local")
        else:  # time_reversal(copy or Download)
            self.result.append("time_reversal")
            self.result.append("time_reversal")

    def operating_system(self):
        for file_name in self.filelist:
            if '__MACOSX' in file_name.filename:  # MAC
                extra1, extra2 = self.check_local_extra_field(file_name.filename, True)
                if extra1 and extra2:
                    self.result.append("MAC")
                    self.compression_method()
                elif extra1 or extra2:
                    self.result.append("Unknown(only one flag)")  # github download
                    self.result.append("Unknown")
                else:
                    self.result.append("Unknown")
                    self.result.append("Unknown")
                return self.result

        for file_name in self.LFH.keys():
            extra1, extra2 = self.check_local_extra_field(file_name, True)
            if extra1 and extra2:  # Linux
                self.result.append("Linux")
                self.compression_method()
            elif extra1 or extra2:
                self.result.append("Unknown(only one flag)")  # github download
                self.result.append("Unknown")
            else:
                break
            return self.result

        #self.result.append("Windows")  # Windows
        self.is_korean_file()
        return self.result

    def compression_method(self):
        # 마우스 우 클릭 압축 시, 데이터 디스크립터 생성, UT 길이 : 0x0D
        data_len = 0
        extra2_start_offset = 0
        is_data_descriptor = False
        terminal = False
        mouse = False
        with open(self.path, 'rb') as zf:
            zf_data = zf.read()
            match = re.findall(b'\x50\x4B\x07\x08', zf_data)
            if match:
                is_data_descriptor = True

        for file in self.filelist:
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2:extra2_start_offset+4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x55\x54':
                    if file.extra[extra2_start_offset + 2 :extra2_start_offset + 4] == b'\x0D\x00':
                        mouse = True
                    elif file.extra[extra2_start_offset + 2 :extra2_start_offset + 4] == b'\x05\x00':
                        terminal = True

                extra2_start_offset = 4 + extra1_size

        if is_data_descriptor and mouse:
            self.result.append("Unknown")
            self.result.append("mouse")
        elif not(is_data_descriptor) and terminal:
            self.result.append("Unknown")
            self.result.append("terminal")
        else:
            self.result.append("Unknown")

    def is_korean_file(self):
        for file in self.filelist:
            if file.encoding_method == 'ascii':
                pass # 영어 파일명
            elif file.encoding_method == 'utf-8':
                #self.result.append("Windows English or Windows Korean - Alzip")
                self.result.append("Windows")
                self.result.append("English")
                self.korean_file = file.filename
                self.check_program_1(file)
                return
            elif file.encoding_method == 'EUC-KR':# or 'ISO-8859-1':  # cp949
                #self.result.append("Windows Korean")
                self.result.append("Windows")
                self.result.append("Korean")
                self.korean_file = file.filename
                self.check_program_2(file, file.filename)
                return

        # 한글 파일명 없음
        self.result.append("Windows")
        self.result.append("Unknown")  # 한글 파일이 없기 때문에 윈도우 영어 버전인지 한글 버전인지 구분 불가
        self.check_program_3()  # 한글 파일이 없기 때문에 윈도우 영어 버전인지 한글 버전인지 구분 불가

    def check_local_extra_field(self, filename, flag=None):
        data_len = 0
        extra2_start_offset = 0
        unicode_extra_field = False
        L_extra_field_1 = False
        L_extra_field_2 = False

        if flag:
            while self.LFH[filename]['extra_field_length'] * 2 > data_len:
                big_endian = '%s%s' % (self.LFH[filename]['extra'][extra2_start_offset + 3 * 2: extra2_start_offset + 4 * 2], self.LFH[filename]['extra'][extra2_start_offset + 2 * 2: extra2_start_offset + 3 * 2])
                extra1_size = int(big_endian, 16)
                data_len += (4 * 2 + extra1_size * 2)
                if self.LFH[filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2] == '5554':
                    L_extra_field_1 = True
                elif self.LFH[filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2] == '7578':
                    L_extra_field_2 = True
                extra2_start_offset = data_len
            return L_extra_field_1, L_extra_field_2
        else:
            while self.LFH[filename]['extra_field_length'] * 2 > data_len:
                big_endian = '%s%s' % (
                self.LFH[filename]['extra'][extra2_start_offset + 3 * 2: extra2_start_offset + 4 * 2],
                self.LFH[filename]['extra'][extra2_start_offset + 2 * 2: extra2_start_offset + 3 * 2])
                extra1_size = int(big_endian, 16)
                data_len += (4 * 2 + extra1_size * 2)
                if self.LFH[filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2] == '7570':
                    unicode_extra_field = True
                extra2_start_offset = data_len #  (4 * 2 + extra1_size * 2)
            return unicode_extra_field

    def check_inner_zip_file(self):
        is_zip_file = False
        n_structures = False

        for file in self.filelist:
            if '.zip' in file.filename:  # ZIP 존재
                is_zip_file = True
                with open(self.path, 'rb') as zf:
                    zf_data = zf.read()
                    match = re.findall(b'\x50\x4B\x05\x06', zf_data)
                    if len(match) > 1:  # ZIP 이중 구조 존재
                        n_structures = True  # True, True
                    else:
                        n_structures = False  # True, False
                    return is_zip_file, n_structures

        return is_zip_file, n_structures  # False, False

    def check_empty_folder(self, folder_name):
        count = 0

        for file in self.filelist:
            if folder_name in file.filename:
                count += 1

        if count > 1:
            return False  # 빈폴더 아님
        elif count == 1:
            return True  # 빈폴더

    def check_program_1(self, file):  # E [alzip, bandizip, 7-zip, WINRAR, WINZIP], K [alzip]
        is_folder = False
        is_folder_header = False
        is_empty_folder = False

        if self.check_local_extra_field(file.filename):
            self.result.append("Local_Extra, [bandizip]")  # E [bandizip]
            return
        elif self.check_central_extra_field(file):
            for file in self.filelist:
                if '/' in file.filename:  # 폴더가 존재
                    is_empty_folder = self.check_empty_folder(file.filename)
                    if is_empty_folder:  # 빈폴더는 고려하지 않음
                        continue
                    else:  # 빈폴더가 아님
                        is_folder = True
                        if file.filename.split('/')[-1] == '':  # 폴더 헤더 존재
                            is_folder_header = True


            if not(is_folder):  # 폴더가 존재하지 않음
                self.check_program_1_2()
                return

            if is_folder and is_folder_header:  # 폴더 헤더 존재
                zip_file, n_structures = self.check_inner_zip_file()
                if zip_file and n_structures:
                    self.result.append("Central_Extra, Folder & Header, ZIP file & nStructure, [7-zip, WINRAR]")
                elif zip_file and not(n_structures):
                    self.result.append("Central_Extra, Folder & Header, ZIP file, [7-zip, WINZIP]")
                elif not(zip_file) and not(n_structures):
                    self.result.append("Central_Extra, Folder & Header, [7-zip, WINRAR, WINZIP]")
                else:
                    self.result.append("Unknown")

            elif is_folder and not(is_folder_header): # 폴더는 있으나 헤더는 없음
                self.result.append("Central_Extra, Folder, E, K [alzip]")
                return

    def check_compression_order(self):
        different_order = False
        temp_filelist = list()
        for file in self.filelist:
            temp_filelist.append(file.filename.lower())

        if sorted(temp_filelist) == temp_filelist:
            pass
        else:
            different_order = True

        return different_order

    def check_program_1_2(self):  # 폴더가 존재하지 않음
        # 내부에 ZIP 존재 및 이중 구조 확인
        is_zip_file, n_structures = self.check_inner_zip_file()

        # 압축 순서 구분하기
        different_order = self.check_compression_order()

        if is_zip_file and n_structures and different_order:
            self.result.append("Central_Extra, ZIP file & nStructure, order, E, K [alzip], E [WINRAR]")
        elif is_zip_file and n_structures and not(different_order):
            self.result.append("Central_Extra, ZIP file & nStructure, [alzip, 7-zip, WINRAR]")
        elif is_zip_file and not(n_structures) and different_order:
            self.result.append("Central_Extra, ZIP file, order, E, K [alzip]")
        elif is_zip_file and not(n_structures) and not(different_order):
            self.result.append("Central_Extra, ZIP file, [alzip, 7-zip, WINZIP]")
        elif not(is_zip_file) and different_order:
            self.result.append("Central_Extra, order, E, K [alzip], E [WINRAR]")
        elif not(is_zip_file) and not(different_order):
            self.result.append("Central_Extra, [alzip, 7-zip, WINRAR, WINZIP]")
        else:
            self.result.append("Unknown")

    def check_central_extra_field(self, file, order=None):
        data_len = 0
        extra2_start_offset = 0
        is_NTFS_extra_field = False
        is_unicode_extra_field = False
        is_0A00_first = False

        while file.extra_field_length > data_len:
            extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2: extra2_start_offset + 4], 'little')
            data_len += (4 + extra1_size)
            if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x0A\x00':
                is_NTFS_extra_field = True
                if not(is_unicode_extra_field):
                    is_0A00_first = True  # 0x0A 00이 먼저 나옴
            elif file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x75\x70':
                is_unicode_extra_field = True

            extra2_start_offset = data_len  # 4 + extra1_size

        if order:
            if is_NTFS_extra_field and is_unicode_extra_field:
                return is_0A00_first
            else:  # 0x0A 00이나 0x75 70 중 없는 것이 존재하기 때문에 순서를 구별하는 것이 중요하지 않음
                return None
        else:
            return is_NTFS_extra_field

    def check_program_2(self, file, file_name):
        is_zip_file = False
        is_NTFS_extra_field = False

        if self.check_local_extra_field(file_name):
            rtn = self.check_central_extra_field(file, True)
            if rtn == None:
                pass
            elif not(rtn):
                self.result.append("Local_Extra, Central_Extra_order, [WINZIP]")
                return
            else:
                is_zip_file, n_structures = self.check_inner_zip_file()

                if is_zip_file and n_structures:
                    self.result.append("Local_Extra, ZIP file & nStructure, [WINRAR]")
                elif is_zip_file and not(n_structures):
                    self.result.append("Local_Extra, ZIP file, [bandizip]")
                elif not(is_zip_file):
                    self.result.append("Local_Extra, [bandizip, WINRAR]")
                else:
                    self.result.append("Unknown")

        else:  # 0x0A 00 존재 여부만 확인
            if file.extra_field_length > 0:
                is_NTFS_extra_field = self.check_central_extra_field(file)
                if is_NTFS_extra_field:
                    self.result.append("Central_Extra, [7-zip]")
                else:
                    self.result.append("Unknown")
                return
            else:
                self.result.append("No_Central_Extra, [Default]")
                return

    def check_program_3(self):
        is_NTFS_extra_field = False
        is_folder = False
        is_folder_header = False
        is_zip_file = False
        n_structures = False

        different_order = self.check_compression_order()

        for file in self.filelist:
            if file.extra_field_length > 0:
                is_NTFS_extra_field = self.check_central_extra_field(file)
                if is_NTFS_extra_field:
                    break
            else:
                self.result.append("No_Central_Extra, [Default]")
                return

        for file in self.filelist:
            if '/' in file.filename:  # 폴더가 존재
                is_empty_folder = self.check_empty_folder(file.filename)
                if is_empty_folder:  # 빈폴더는 고려하지 않음
                    continue
                else:
                    is_folder = True
                    if file.filename.split('/')[-1] == '':  # 폴더 헤더 존재
                        is_folder_header = True


        if is_NTFS_extra_field:
            if is_folder:
                if not(is_folder_header):
                    self.result.append("Folder, E, K [alzip]")
                elif is_zip_file and n_structures:
                    self.result.append("Folder & Header, ZIP file & nStructure, [7-zip, WINRAR]")
                elif is_zip_file and not(n_structures):
                    self.result.append("Folder & Header, ZIP file, [bandizip, WINZIP]")
                elif not(is_zip_file):
                    self.result.append("Folder & Header, [bandizip, 7-zip, WINRAR, WINZIP]")
                else:
                    self.result.append("Unknown")
            else:
                if is_zip_file and n_structures and different_order:
                    self.result.append("ZIP file & nStructure, order, E, K [alzip, WINRAR]")
                elif is_zip_file and n_structures and not(different_order):
                    self.result.append("ZIP file & nStructure, [alzip, 7-zip, WINRAR]")
                elif is_zip_file and not(n_structures) and different_order:
                    self.result.append("ZIP file, order [alzip]")
                elif is_zip_file and not(n_structures) and not(different_order):
                    self.result.append("ZIP file, [alzip, bandizip, 7-zip, WINZIP]")
                elif not(is_zip_file):
                    self.result.append("Central_Extra, [alzip, bandizip, 7-zip, WINRAR, WINZIP]")
                else:
                    self.result.append("Unknown")

        elif not(is_NTFS_extra_field):
            self.result.append("No_Central_Extra, [Default]")

if __name__ == "__main__":
    result = dict()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", action="store", type=str)
    parser.add_argument("-f", dest="file", action="store", type=str)
    parser.add_argument("-v", dest="volume", action="store", type=str)
    args = parser.parse_args()

    if args.dir:
        for root, _, files in os.walk(args.dir):
            for file in files:
                if file.split('.')[-1].lower() == 'zip':
                    full_path = os.path.join(root, file)
                    cs = check_source(full_path)
                    cs.created_env()
                    cs.stored_header()
                    result[full_path] = cs.operating_system()

    elif args.file:
        cs = check_source(args.file)
        cs.created_env()
        cs.stored_header()
        result[args.file] = cs.operating_system()

    elif args.volume:
        for root, _, files in os.walk(args.volume):
            if 'OneDrive - 고려대학교' in root or 'AppData' in root:
                continue
            else:
                for file in files:
                    if file.split('.')[-1].lower() == 'zip':
                        try:
                            full_path = os.path.join(root, file)
                            cs = check_source(full_path)
                            cs.created_env()
                            cs.stored_header()
                            result[full_path] = cs.operating_system()
                        except:
                            pass

    for k, v in result.items():
        print(k, v)

    temp = dict()
    import csv
    f = open('output.csv', 'w', encoding='utf8', newline='')
    wr = csv.writer(f)
    wr.writerow(['Time', 'From', 'OS', 'Language', 'method'])
    for num, list in enumerate(result.values()):
        wr.writerow(list)
    f.close()
    #     r = ''
    #     for i in range(0,len(list)):
    #         r += list[i]
    #     try:
    #         temp[r] += 1
    #     except:
    #         temp[r] = 1
    #
    # for k, v in temp.items():
    #     print(k, v)
    #
    # print(len(result.values()))
