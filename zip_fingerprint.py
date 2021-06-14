from custom_zipfile import ZipFile
import os
import re
import argparse
from datetime import datetime, timedelta
from file_list import rtn_program
import csv

class check_source:
    def __init__(self, path):
        self.path = path
        self.LFH = dict()
        self.zip = ZipFile(self.path)
        self.filelist = ZipFile.infolist(self.zip)
        self.result = list()
        self.korean_file = ""

    def stored_header(self):
        for file in self.filelist:
            self.zip.open(file.filename)
            self.Local_Header(self.zip.min_lfh)

    def Local_Header(self, file):
        self.LFH[file["filename"]] = file

    def check_creating_system(self):
        creating_system = list()
        for file in self.filelist:
            creating_system.append(file.create_system)

        creating_system = list(set(creating_system))

        if len(creating_system) == 1:
            return creating_system[0]
        else:
            return 'N/A'

    def is_korean_file(self):
        for file in self.filelist:
            if file.encoding_method == 'ascii':
                pass
            elif file.encoding_method == 'utf-8':
                self.korean_file = file
                return 'UTF8'
            elif file.encoding_method in ['EUC-KR', 'ISO-8859-1']:
                self.korean_file = file
                return 'CP949'
        return 'UTF8'  # no korean file

    def check_local_extra_field(self, uid=False):
        id_list = list()
        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0

            if not(uid):
                while self.LFH[file.filename]['extra_field_length'] * 2 > data_len:
                    big_endian = '%s%s' % (self.LFH[file.filename]['extra'][extra2_start_offset + 3 * 2: extra2_start_offset + 4 * 2], self.LFH[file.filename]['extra'][extra2_start_offset + 2 * 2: extra2_start_offset + 3 * 2])
                    extra1_size = int(big_endian, 16)
                    data_len += (4 * 2 + extra1_size * 2)
                    id_list.append(self.LFH[file.filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2])
                    extra2_start_offset = data_len
            else:
                while self.LFH[file.filename]['extra_field_length'] * 2 > data_len:
                    big_endian = '%s%s' % (self.LFH[file.filename]['extra'][extra2_start_offset + 3 * 2: extra2_start_offset + 4 * 2], self.LFH[file.filename]['extra'][extra2_start_offset + 2 * 2: extra2_start_offset + 3 * 2])
                    extra1_size = int(big_endian, 16)
                    data_len += (4 * 2 + extra1_size * 2)
                    if self.LFH[file.filename]['extra'][extra2_start_offset:extra2_start_offset + 2 * 2] == '5558':
                        uid_big = '%s%s' % (self.LFH[file.filename]['extra'][extra2_start_offset + 13 * 2: extra2_start_offset + 14 * 2], self.LFH[file.filename]['extra'][extra2_start_offset + 12 * 2: extra2_start_offset + 13 * 2])
                        gid_big = '%s%s' % (self.LFH[file.filename]['extra'][extra2_start_offset + 15 * 2: extra2_start_offset + 16 * 2], self.LFH[file.filename]['extra'][extra2_start_offset + 14 * 2: extra2_start_offset + 15 * 2])
                    extra2_start_offset = data_len
                return int(uid_big, 16), int(gid_big,16)

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
            if '.zip' in file.filename:
                with open(self.path, 'rb') as zf:
                    zf_data = zf.read()
                    match = re.findall(b'\x50\x4B\x05\x06', zf_data)
                    if len(match) > 1:
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
            return False
        elif count == 1:
            return True

    def check_header_of_folder(self):
        for file in self.filelist:
            if '/' in file.filename:
                is_empty_folder = self.check_empty_folder(file.filename)
                if is_empty_folder:
                    continue
                else:
                    if file.filename.split('/')[-1] == '':
                        return "folder_with_header"
                    else:
                        return "folder_without_header"
        return "N/A"

    def check_compression_order(self):
        different_order = False
        temp_filelist = list()

        for file in self.filelist:
            if '__macosx/' not in file.filename.lower():
                temp_filelist.append(file.filename.lower())

        if sorted(temp_filelist) == temp_filelist:
            pass
        else:
            different_order = True

        return different_order

    def check_time_nanoseconds(self):
        time_list = list()
        exist_time_extra = False
        for file in self.filelist:
            data_len = 0
            extra2_start_offset = 0
            while file.extra_field_length > data_len:
                extra1_size = int.from_bytes(file.extra[extra2_start_offset + 2: extra2_start_offset + 4], 'little')
                data_len += (4 + extra1_size)
                if file.extra[extra2_start_offset:extra2_start_offset + 2] == b'\x0A\x00':
                    exist_time_extra = True
                    time_length = extra2_start_offset + 10
                    time_start_offset = time_length + 2

                    time_count = int(int.from_bytes(file.extra[time_length:time_length+2], byteorder='little') / 8)
                    for i in range(time_count):
                        temp_time = int.from_bytes(file.extra[time_start_offset + (i*8) :time_start_offset + ((i+1)*8)], byteorder='little')
                        nanoseconds = (datetime(1601, 1, 1) + timedelta(microseconds=temp_time / 10)).strftime("%f")
                        time_list.append(nanoseconds)

                extra2_start_offset = data_len  # 4 + extra1_size

        if not(exist_time_extra):
            return "N/A"

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
                    uid_len = int.from_bytes(file.extra[extra2_start_offset+5:extra2_start_offset + 6], byteorder='little')
                    uid.append(int.from_bytes(file.extra[extra2_start_offset+6:extra2_start_offset+6+uid_len], byteorder='little'))
                    gid_len = int.from_bytes(file.extra[extra2_start_offset+6+uid_len:extra2_start_offset +6+uid_len+1], byteorder='little')
                    gid.append(int.from_bytes(file.extra[extra2_start_offset+6+uid_len+1:extra2_start_offset+6+uid_len+1+gid_len], byteorder='little'))

                extra2_start_offset = data_len
        uid = list(set(uid))
        gid = list(set(gid))

        if (len(uid) == 1 and len(gid) == 1) and (uid[0] in [1000, 501]) and (gid[0] in [1000, 20]):
            return uid[0], gid[0]
        else:
            return "N/A"

    def check_os_folder(self):
        for file_name in self.filelist:
            if '__MACOSX' in file_name.filename:  # MAC
                return '__MACOSX'

        return 'N/A'

    def check_data_descriptor(self):
        file_count = 0
        for file in self.filelist:
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
        result['reason'].append(local_extra_id)
        creating_sys = self.check_creating_system()
        result['reason'].append(creating_sys)
        if local_extra_id == '7570' or local_extra_id == 'N/A' and creating_sys == 0:
            encoding_method = self.is_korean_file()
            if self.korean_file:
                result['reason'].append("korean_file")
            else:
                result['reason'].append("no_korean_file")
            result['reason'].append(self.check_central_extra_field())
            result['reason'].append(self.check_time_nanoseconds())
            result['reason'].append(encoding_method)
            result['reason'].append(self.check_header_of_folder())
            result['reason'].append(self.check_inner_zip_file())
            order_rtn = self.check_compression_order()
            if not(order_rtn): result['reason'].append('alphabetical_order')
            else: result['reason'].append('different_order')

        elif local_extra_id == 'N/A' and creating_sys == 3:  # macOS_winzip
            result['reason'].append(self.check_header_of_folder())
            result['reason'].append(self.check_inner_zip_file())
            order_rtn = self.check_compression_order()
            if not (order_rtn): result['reason'].append('alphabetical_order')
            else: result['reason'].append('different_order')

        elif local_extra_id == ['5554', '7578']:
            result['reason'].append(self.length_of_extra_field())
            result['reason'].append(self.check_uid())
            result['reason'].append(self.check_inner_zip_file())
            result['reason'].append(self.check_os_folder())
            result['reason'].append(self.check_data_descriptor())

        elif local_extra_id == ['5558']:
            result['reason'].append(self.check_local_extra_field(uid=True))
            result['reason'].append(self.check_header_of_folder())
            result['reason'].append(self.check_inner_zip_file())
            order_rtn = self.check_compression_order()
            if not(order_rtn): result['reason'].append('alphabetical_order')
            else: result['reason'].append('different_order')
        else:
            result['program'] = ['N/A']
            return result

        a = rtn_program()
        a.program_list()
        result["program"] = a.rtn_(result['reason'])

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

    if args.dir:
        for root, _, files in os.walk(args.dir):
            if 'set9' in root or 'set2' in root or 'set4' in root or 'paper' in root:
                continue
            else:
                for file in files:
                    if file.split('.')[-1].lower() == 'zip':
                        full_path = os.path.join(root, file)
                        cs = check_source(full_path)
                        cs.stored_header()
                        result[file] = cs.presume_program()

    elif args.file:
        cs = check_source(args.file)
        cs.stored_header()
        result[args.file] = cs.presume_program()

    elif args.volume:
        for root, _, files in os.walk(args.volume):
            if 'OneDrive - 고려대학교' in root or 'AppData' in root:
                continue
            if 'Desktop' in root or 'Documents' in root or 'Downloads' in root:
                for file in files:
                    if file.split('.')[-1].lower() == 'zip':
                        full_path = os.path.join(root, file)
                        cs = check_source(full_path)
                        cs.stored_header()
                        result[file] = cs.presume_program()

    print(result)