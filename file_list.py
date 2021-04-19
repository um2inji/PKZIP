# lt['reason'].append("korean_file")
#         else:
#             result['reason'].append("no_korean_file")
# # encoding_method = 'UTF', 'CP'
#         result['reason'].append(self.check_local_extra_field())  # local_extra_field_id = ['5554', '7578'], ['7570'], ["N/A"]
#         result['reason'].append(self.check_central_extra_field() ) # central_extra_field_id = '0X0A00+0x7075', '0x7075+0x0A00', '0x0A00', 'none
#         result['reason'].append(self.check_inner_zip_file() ) # double_zipping = ['zip', 'n_structures'], ['zip'], ['no_double_zip']
#         result['reason'].append(self.check_header_of_folder())  # folder_info = 'folder_without_header', 'folder_with_header', 'no_folder'
#         order_rtn = self.check_compression_order()  # True, False
#         if not(order_rtn): result['reason'].append('ascii_order') #order = 'ascii_order'
#         else: result['reason'].append('different_order') #order = 'different_order'
#         if result['reason'][2] == ['7570']:
#             result['reason'].append(self.check_time_nanoseconds())  # nanoseconds = 'all', 'part', 'N/A'

class rtn_program:
    def __init__(self):
        self.program = dict()
        self.program['windows_bandi'] = list()
        self.program['windows_winrar'] = list()
        self.program['windows_winzip'] = list()
        self.program['windows_7zip'] = list()
        self.program['windows_compress'] = list()
        self.program['windows_alzip'] = list()
        self.program['macOS_zip'] = list()
        self.program['macOS_compress'] = list()
        self.program['linux_zip'] = list()
        self.program['linux_compress'] = list()

    def program_list(self):
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'UTF8', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
    
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header','ascii_order', 'nanoseconds'])
    
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_bandi'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'folder_with_header','ascii_order', 'nanoseconds'])
    
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'different_order', 'nanoseconds'])
    
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'different_order', 'nanoseconds'])
    
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['no_double_zip'], 'folder_with_header', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'no_folder', 'different_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_winrar'].append([['7570'], 'CP949', 'korean_file', '0x0A00+0x7570', ['zip', 'n_structures'], 'folder_with_header', 'different_order', 'nanoseconds'])
    
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
    
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
    
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['zip', 'n_structures'], 'folder_with_header','ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['zip'], 'no_folder', 'ascii_order', 'part_nanoseconds'])
        self.program['windows_winzip'].append([['7570'], 'CP949', 'korean_file', '0x7570+0x0A00', ['zip'], 'folder_with_header','ascii_order', 'part_nanoseconds'])
    
    
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
    
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
    
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_with_header','ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'nanoseconds'])
        self.program['windows_7zip'].append([["N/A"], 'CP949', 'korean_file', '0x0A00', ['zip'], 'folder_with_header','ascii_order', 'nanoseconds'])
    

        self.program['windows_compress'].append([["N/A"], 'UTF8', 'korean_file', 'N/A', ['no_double_zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'korean_file', 'N/A', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'korean_file', 'N/A', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'korean_file', 'N/A', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])
    
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'no_korean_file', 'N/A', ['no_double_zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'no_korean_file', 'N/A', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'no_korean_file', 'N/A', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'UTF8', 'no_korean_file', 'N/A', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])
    
        self.program['windows_compress'].append([["N/A"], 'CP949', 'korean_file', 'N/A', ['no_double_zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'CP949', 'korean_file', 'N/A', ['no_double_zip'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'CP949', 'korean_file', 'N/A', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_compress'].append([["N/A"], 'CP949', 'korean_file', 'N/A', ['zip', 'n_structures'], 'folder_with_header', 'ascii_order', 'no_nanoseconds'])

        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['no_double_zip'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'korean_file', '0x0A00', ['zip'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])
    
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['no_double_zip'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip', 'n_structures'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'no_folder', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'no_folder', 'ascii_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'folder_without_header', 'different_order', 'no_nanoseconds'])
        self.program['windows_alzip'].append([["N/A"], 'UTF8', 'no_korean_file', '0x0A00', ['zip'], 'folder_without_header', 'ascii_order', 'no_nanoseconds'])

        self.program['macOS_zip'].append([['5554', '7578'], 'no_os_folder', 'no_data_descriptor', '0x0500'])
        self.program['macOS_compress'].append([['5554', '7578'], '__MACOSX', 'data_descriptor', '0x0D00'])
        self.program['linux_zip'].append([['5554', '7578'], 'no_os_folder', 'no_data_descriptor', '0x0500'])
        self.program['linux_compress'].append([['5554', '7578'], 'no_os_folder', 'data_descriptor', '0x0D00'])

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

