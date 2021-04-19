from custom_zipfile import ZipFile, BadZipFile
import os
import chardet # pip install
import re
import argparse
from pyads import ADS
from datetime import datetime, timedelta
from file_list import rtn_program

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

    def is_korean_file(self):
        for file in self.filelist:
            if file.encoding_method == 'ascii':
                pass # 영어 파일명
            elif file.encoding_method == 'utf-8':
                self.korean_file = file
                return 'UTF8'
            elif file.encoding_method in ['EUC-KR', 'ISO-8859-1']:  # cp949
                self.korean_file = file
                return 'CP949'

        return 'UTF8'  # no korean file

    def check_local_extra_field(self):
        id_list = list()
        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0

            while self.LFH[file.filename]['extra_field_length'] * 2 > data_len:
                big_endian = '%s%s' % (self.LFH[file.filename]['extra'][extra2_start_offset + 3 * 2: extra2_start_offset + 4 * 2], self.LFH[file.filename]['extra'][extra2_start_offset + 2 * 2: extra2_start_offset + 3 * 2])
                extra1_size = int(big_endian, 16)
                data_len += (4 * 2 + extra1_size * 2)
                id_list.append(self.LFH[file.filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2])
                extra2_start_offset = data_len

        if id_list:
            id_list = list(set(id_list))
            id_list = sorted(id_list)
            return id_list
        else:
            return ["N/A"]

    def check_central_extra_field(self):
        is_NTFS_extra_field = False
        is_unicode_extra_field = False

        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2: extra2_start_offset + 4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x0A\x00':
                    is_NTFS_extra_field = True
                elif file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x75\x70':
                    is_unicode_extra_field = True
                extra2_start_offset = data_len

        if is_NTFS_extra_field and is_unicode_extra_field:
            if self.korean_file.extra[:2] == b'\x0A\x00':
                return '0x0A00+0x7570'
            else:
                return '0x7570+0x0A00'
        elif is_NTFS_extra_field and not(is_unicode_extra_field):
            return '0x0A00'
        elif not(is_NTFS_extra_field) and not(is_unicode_extra_field):
            return 'N/A'

    def check_inner_zip_file(self):
        is_zip_file = False
        n_structures = False
        result = list()

        for file in self.filelist:
            if '.zip' in file.filename:  # ZIP 존재
                #is_zip_file = True
                result.append("zip")
                with open(self.path, 'rb') as zf:
                    zf_data = zf.read()
                    match = re.findall(b'\x50\x4B\x05\x06', zf_data)
                    if len(match) > 1:  # ZIP 이중 구조 존재
                        #n_structures = True  # True, True
                        result.append("n_structures")
                    else:
                        pass
                        #n_structures = False  # True, False
                    return result

        result.append('no_double_zip')
        return result # False, False

    def check_empty_folder(self, folder_name):
        count = 0

        for file in self.filelist:
            if folder_name in file.filename:
                count += 1

        if count > 1:
            return False  # 빈폴더 아님
        elif count == 1:
            return True  # 빈폴더

    def check_header_of_folder(self):
        is_folder = False
        is_folder_header = False

        for file in self.filelist:
            if '/' in file.filename:  # 폴더가 존재
                is_empty_folder = self.check_empty_folder(file.filename)
                if is_empty_folder:  # 빈폴더는 고려하지 않음
                    continue
                else:
                    #is_folder = True
                    if file.filename.split('/')[-1] == '':  # 폴더 헤더 존재
                        is_folder_header = True
                        return "folder_with_header"
                    else:
                        return "folder_without_header"
        return "no_folder"
        #return is_folder, is_folder_header

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

    def check_time_nanoseconds(self):
        time_list = list()
        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2: extra2_start_offset + 4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x0A\x00':
                    time_length = extra2_start_offset + 10
                    time_start_offset = time_length + 2

                    time_count = int(int.from_bytes(file.extra[time_length:time_length+2], byteorder='little') / 8)
                    for i in range(time_count):
                        temp_time = int.from_bytes(file.extra[time_start_offset + (i*8) :time_start_offset + ((i+1)*8)], byteorder='little')
                        nanoseconds = (datetime(1601, 1, 1) + timedelta(microseconds=temp_time / 10)).strftime("%f")
                        time_list.append(nanoseconds)
                extra2_start_offset = data_len  # 4 + extra1_size

        count_dict = dict()
        count_dict["all"] = 0
        count_dict["part"] = 0
        count_dict["none"] = 0

        for time in time_list:
            if time == "000000":
                count_dict["all"] += 1
            elif time[3:] == "000":
                count_dict["part"] += 1
            else:
                count_dict["none"] += 1

        if count_dict["all"] == len(time_list):
            return 'no_nanoseconds'
        elif count_dict["part"] + count_dict["all"] == len(time_list):
            return 'part_nanoseconds'
        else:
            return 'nanoseconds'

    def check_os_folder(self):
        for file_name in self.filelist:
            if '__MACOSX' in file_name.filename:  # MAC
                return '__MACOSX'

        return 'no_os_folder'

    def check_data_descriptor(self):
        # 마우스 우 클릭 압축 시, 데이터 디스크립터 생성
        is_data_descriptor = False
        file_count = 0
        for file in self.filelist:  # 폴더를 제외한 파일의 개수
            if '/' in file.filename:
                if file.filename.split('/')[-1] != '':
                    file_count += 1
            else:
                file_count += 1

        with open(self.path, 'rb') as zf:
            zf_data = zf.read()
            match = re.findall(b'\x50\x4B\x07\x08', zf_data)
            print(len(match), file_count)
            if len(match) >= file_count:
                return "data_descriptor"

        return "no_data_descriptor"

    def compression_method(self):
        # 마우스 우 클릭 압축 시, UT 길이 : 0x0D(central)
        data_len = 0
        extra2_start_offset = 0

        for file in self.filelist:
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2:extra2_start_offset+4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x55\x54':
                    if file.extra[extra2_start_offset + 2 :extra2_start_offset + 4] == b'\x0D\x00':
                        return '0x0D00'
                    elif file.extra[extra2_start_offset + 2 :extra2_start_offset + 4] == b'\x05\x00':
                        return '0x0500'

                extra2_start_offset = 4 + extra1_size

    def presume_program(self):
        result = dict()
        result['reason'] = list()

        local_extra_id = self.check_local_extra_field()
        result['reason'].append(local_extra_id)  # local_extra_field_id = ['5554', '7578'], ['7570'], []
        if local_extra_id == ['7570'] or local_extra_id == ['N/A']:
            result['reason'].append(self.is_korean_file())  # encoding_method = 'UTF', 'CP'
            if self.korean_file:
                result['reason'].append("korean_file")
            else:
                result['reason'].append("no_korean_file")
            result['reason'].append(self.check_central_extra_field()) # central_extra_field_id = '0X0A00+0x7075', '0x7075+0x0A00', '0x0A00', 'none
            result['reason'].append(self.check_inner_zip_file()) # double_zipping = ['zip', 'n_structures'], ['zip'], ['no_double_zip']
            result['reason'].append(self.check_header_of_folder())  # folder_info = 'folder_without_header', 'folder_with_header', 'no_folder'
            order_rtn = self.check_compression_order()  # True, False
            if not(order_rtn): result['reason'].append('ascii_order') #order = 'ascii_order'
            else: result['reason'].append('different_order') #order = 'different_order'
            result['reason'].append(self.check_time_nanoseconds())  # 'no_nanoseconds', 'part_nanoseconds', 'nanoseconds'

        elif local_extra_id == ['5554', '7578']:
            result['reason'].append(self.check_os_folder())
            result['reason'].append(self.check_data_descriptor())
            result['reason'].append(self.compression_method())

        else:
            result['program'] = ['can\'t presume the program!']
            return result

        a = rtn_program()
        a.program_list()
        result["program"] = a.rtn_(result['reason'])
        return result

def write_cvs(result, win_wr, unix_wr):
    temp = dict()
    temp['total'] = list()

    # win_wr.writerow()
    # unix_wr.writerow()

    for i in result['reason']:
        temp['total'].append(i)
    temp['total'].append(result['program'])
    print(temp)

    #try:
    if '5554' in result['reason'][0]:
        unix_wr.writerow(temp['total'])
    else:
        win_wr.writerow(temp['total'])
    #     print('error', e)

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


if __name__ == "__main__":
    result = dict()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", action="store", type=str)
    parser.add_argument("-f", dest="file", action="store", type=str)
    parser.add_argument("-v", dest="volume", action="store", type=str)
    args = parser.parse_args()
    import csv

    win_f = open('windows_output.csv', 'w', encoding='utf8', newline='')
    unix_f = open('unix_output.csv', 'w', encoding='utf8', newline='')
    win_wr = csv.writer(win_f)
    unix_wr = csv.writer(unix_f)
    win_wr.writerow(['local_extra', 'encoding', 'korean_file', 'central_extra', 'double_zip','folder', 'order', 'seconds', 'program'])
    unix_wr.writerow(['local_extra', 'os_folder', 'data_descriptor', 'length_extra_field', 'program'])
    if args.dir:
        for root, _, files in os.walk(args.dir):
            if 'set9' in root or 'set2' in root or 'set4' in root:
                continue
            else:
                for file in files:
                    if file.split('.')[-1].lower() == 'zip':
                        full_path = os.path.join(root, file)
                        print(file)
                        cs = check_source(full_path)
                        cs.stored_header()
                        result = cs.presume_program()
                        write_cvs(result, win_wr, unix_wr)

    elif args.file:
        cs = check_source(args.file)
        cs.stored_header()
        result = cs.presume_program()
        write_cvs(result, win_wr, unix_wr)

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
                            cs.stored_header()
                            result = cs.presume_program()
                            write_cvs(result, win_wr, unix_wr)
                        except:
                            pass

    win_f.close()
    unix_f.close()