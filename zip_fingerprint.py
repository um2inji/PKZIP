from custom_zipfile import ZipFile, BadZipFile
import os
import chardet # pip install
import re
import argparse
from pyads import ADS
from datetime import datetime, timedelta
from file_list import rtn_program
import csv


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
                print('??', file.filename)
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

        if len(id_list) == 1:
            return id_list[0]
        elif len(id_list) >= 2:
            id_list = list(set(id_list))
            id_list = sorted(id_list)
            return id_list
        else:
            return "N/A"

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
        for file in self.filelist:
            if '.zip' in file.filename:  # ZIP 존재
                with open(self.path, 'rb') as zf:
                    zf_data = zf.read()
                    match = re.findall(b'\x50\x4B\x05\x06', zf_data)
                    if len(match) > 1:  # ZIP 이중 구조 존재
                        return 'no_double_zipping'
                    else:
                        return 'double_zipping'
        return 'N/A'


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
        for file in self.filelist:
            if '/' in file.filename:  # 폴더가 존재
                is_empty_folder = self.check_empty_folder(file.filename)
                if is_empty_folder:  # 빈폴더는 고려하지 않음
                    continue
                else:
                    if file.filename.split('/')[-1] == '':  # 폴더 헤더 존재
                        return "folder_with_header"
                    else:
                        return "folder_without_header"
        return "N/A"

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
            return '.0000000'
        elif count_dict["part"] + count_dict["all"] == len(time_list):
            return '.fff0000'
        else:
            return '.fffffff'

    def check_uid(self):
        uid = list()
        gid = list()
        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2: extra2_start_offset + 4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x75\x78':
                    uid.append(int.from_bytes(file.extra[extra2_start_offset+6:extra2_start_offset+10], byteorder='little'))
                    gid.append(int.from_bytes(file.extra[extra2_start_offset+11:extra2_start_offset+15], byteorder='little'))

                extra2_start_offset = data_len
        uid = list(set(uid))
        gid = list(set(gid))

        if len(uid) == 1 and len(gid) == 1:
            return uid[0], gid[0]
        else:
            return "N/A"

    def check_os_folder(self):
        for file_name in self.filelist:
            if '__MACOSX' in file_name.filename:  # MAC
                return '__MACOSX'

        return 'N/A'

    def check_data_descriptor(self):
        # 마우스 우 클릭 압축 시, 데이터 디스크립터 생성
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

            if len(match) >= file_count:
                return "data_descriptor"

        return "N/A"

    def length_of_extra_field(self):
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
        if local_extra_id == '7570' or local_extra_id == 'N/A':
            encoding_method = self.is_korean_file()
            if self.korean_file:
                result['reason'].append("korean_file")
            else:
                result['reason'].append("no_korean_file")
            result['reason'].append(self.check_central_extra_field()) # central_extra_field_id = '0X0A00+0x7075', '0x7075+0x0A00', '0x0A00', 'none
            result['reason'].append(self.check_time_nanoseconds())  # 'no_nanoseconds', 'part_nanoseconds', 'nanoseconds'
            result['reason'].append(encoding_method)  # encoding_method = 'UTF', 'CP'
            result['reason'].append(self.check_header_of_folder())  # folder_info = 'folder_without_header', 'folder_with_header', 'no_folder'
            result['reason'].append(self.check_inner_zip_file()) # double_zipping = ['zip', 'n_structures'], ['zip'], ['no_double_zip']
            order_rtn = self.check_compression_order()  # True, False
            if not(order_rtn): result['reason'].append('alphabetical_order') #order = 'ascii_order'
            else: result['reason'].append('different_order') #order = 'different_order'

        elif local_extra_id == ['5554', '7578']:
            result['reason'].append(self.length_of_extra_field())  # 0x0D00, 0x0500
            result['reason'].append(self.check_uid())
            result['reason'].append(self.check_inner_zip_file())
            result['reason'].append(self.check_os_folder())  #  __MACOSX, 'no_os_folder'
            result['reason'].append(self.check_data_descriptor())  # data_desciptor, no_data_descriptor


        else:
            result['program'] = ['N/A']
            return result

        a = rtn_program()
        a.program_list()
        result["program"] = a.rtn_(result['reason'])
        print(result)
        return result

def write_cvs(result, win_wr, unix_wr):
    temp = dict()
    temp['total'] = list()

    for i in result['reason']:
        temp['total'].append(i)
    temp['total'].append(result['program'])

    #try:
    if '5554' in result['reason'][0]:
        unix_wr.writerow(temp['total'])
    else:
        win_wr.writerow(temp['total'])

if __name__ == "__main__":
    result = dict()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", action="store", type=str)
    parser.add_argument("-f", dest="file", action="store", type=str)
    parser.add_argument("-v", dest="volume", action="store", type=str)
    args = parser.parse_args()

    win_f = open('windows_output.csv', 'w', encoding='utf8', newline='')
    unix_f = open('unix_output.csv', 'w', encoding='utf8', newline='')
    win_wr = csv.writer(win_f)
    unix_wr = csv.writer(unix_f)
    win_wr.writerow(['local_extra', 'korean_file', 'central_extra', 'seconds', 'encoding', 'folder', 'double_zip', 'order', 'program'])
    unix_wr.writerow(['local_extra', 'length_extra_field', 'double_zip', 'os_folder', 'data_descriptor',  'program'])
    if args.dir:
        for root, _, files in os.walk(args.dir):
            if 'set9' in root or 'set2' in root or 'set4' in root or 'paper' in root:
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
    t = ''
    d = dict()
    f = open('windows_output.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        t = ''
        for i in line:
            t += i
        try:
            d[t] += 1
        except:
            d[t] = 1
    for k, v in d.items():
        print(k, v)
    f.close()
    f = open('unix_output.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        t = ''
        for i in line:
            t += i
        try:
            d[t] += 1
        except:
            d[t] = 1
    for k, v in d.items():
        print(k, v)
    f.close()
