class rtn_program:
    def __init__(self):
        self.program = dict()
        self.program['Windows_Bandizip'] = list()
        self.program['Windows_WinRAR'] = list()
        self.program['Windows_WinZip'] = list()
        self.program['Windows_7zip'] = list()
        self.program['Windows_Compressed_folder'] = list()
        self.program['macOS_zip'] = list()
        self.program['macOS_Compress'] = list()
        self.program['Ubuntu_zip'] = list()
        self.program['Ubuntu_Compress'] = list()
        self.program['macOS_Bandizip'] = list()
        self.program['macOS_WinZip'] = list()

    def program_list(self):
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order', ])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
    
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Bandizip'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
    
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'different_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinRAR'].append(['7570', 0, 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_WinZip'].append(['7570', 0, 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'double_zipping','alphabetical_order'])
    
    
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['Windows_7zip'].append(["N/A", 0, 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'double_zipping','alphabetical_order'])
    

        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'no_korean_file', 'N/A', 'N/A', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'no_korean_file', 'N/A', 'N/A', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'no_korean_file', 'N/A', 'N/A', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'no_korean_file', 'N/A', 'N/A', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['Windows_Compressed_folder'].append(["N/A", 0, 'korean_file', 'N/A', 'N/A', 'CP949', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])

        self.program['macOS_zip'].append([['5554', '7578'], 3, '0x0500', (501, 20), 'no_double_zipping', 'N/A', 'N/A'])
        self.program['macOS_zip'].append([['5554', '7578'], 3, '0x0500', (501, 20), 'N/A', 'N/A', 'N/A'])
        self.program['macOS_Compress'].append([['5554', '7578'], 3, '0x0D00', (501, 20), 'double_zipping', '__MACOSX', 'data_descriptor'])
        self.program['macOS_Compress'].append([['5554', '7578'], 3, '0x0D00', (501, 20), 'N/A', '__MACOSX', 'data_descriptor'])

        self.program['macOS_zip'].append([['5554', '7578'], 3, '0x0500', 'N/A', 'no_double_zipping', 'N/A', 'N/A'])
        self.program['macOS_zip'].append([['5554', '7578'], 3, '0x0500', 'N/A', 'N/A', 'N/A', 'N/A'])
        self.program['macOS_Compress'].append([['5554', '7578'], 3, '0x0D00', 'N/A', 'double_zipping', '__MACOSX', 'data_descriptor'])
        self.program['macOS_Compress'].append([['5554', '7578'], 3, '0x0D00', 'N/A', 'N/A', '__MACOSX', 'data_descriptor'])

        self.program['Ubuntu_zip'].append([['5554', '7578'], 3, '0x0500', (1000, 1000), 'no_double_zipping', 'N/A', 'N/A'])
        self.program['Ubuntu_zip'].append([['5554', '7578'], 3, '0x0500', (1000, 1000), 'N/A', 'N/A', 'N/A'])
        self.program['Ubuntu_Compress'].append([['5554', '7578'], 3, '0x0D00', (1000, 1000), 'double_zipping', 'N/A', 'data_descriptor'])
        self.program['Ubuntu_Compress'].append([['5554', '7578'], 3, '0x0D00', (1000, 1000), 'N/A', 'N/A', 'data_descriptor'])

        self.program['Ubuntu_zip'].append([['5554', '7578'], 3, '0x0500', 'N/A', 'no_double_zipping', 'N/A', 'N/A'])
        self.program['Ubuntu_zip'].append([['5554', '7578'], 3, '0x0500', 'N/A', 'N/A', 'N/A', 'N/A'])
        self.program['Ubuntu_Compress'].append([['5554', '7578'], 3, '0x0D00', 'N/A', 'double_zipping', 'N/A', 'data_descriptor'])
        self.program['Ubuntu_Compress'].append([['5554', '7578'], 3, '0x0D00', 'N/A', 'N/A', 'N/A', 'data_descriptor'])

        self.program['macOS_Bandizip'].append([['5558'], 3, (501, 20), 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['macOS_Bandizip'].append([['5558'], 3, (501, 20), 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['macOS_Bandizip'].append([['5558'], 3, (501, 20), 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['macOS_Bandizip'].append([['5558'], 3, (501, 20), 'N/A', 'N/A', 'alphabetical_order'])

        self.program['macOS_WinZip'].append(['N/A', 3, 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['macOS_WinZip'].append(['N/A', 3, 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['macOS_WinZip'].append(['N/A', 3, 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['macOS_WinZip'].append(['N/A', 3, 'N/A', 'N/A', 'alphabetical_order'])


    def rtn_(self, analysis):
        candidate = list()
        for k, v in self.program.items():
            for _, reason in enumerate(v):
                if analysis == reason:
                    candidate.append(k)

        if candidate:
            return candidate
        else:
            return ["N/A"]

