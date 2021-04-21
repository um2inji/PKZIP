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
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order', ])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
    
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_bandi'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
    
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'different_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winrar'].append(['7570', 'korean_file', '0x0A00+0x7570', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping', 'different_order'])
    
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(["N/A", 'no_korean_file', '0x0A00', '.fff0000', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_winzip'].append(['7570', 'korean_file', '0x7570+0x0A00', '.fff0000', 'CP949', 'folder_with_header', 'double_zipping','alphabetical_order'])
    
    
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'no_korean_file', '0x0A00', '.fffffff', 'UTF8', 'folder_with_header', 'double_zipping', 'alphabetical_order'])
    
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'no_double_zipping','alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_7zip'].append(["N/A", 'korean_file', '0x0A00', '.fffffff', 'CP949', 'folder_with_header', 'double_zipping','alphabetical_order'])
    

        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['windows_compress'].append(["N/A", 'no_korean_file', 'N/A', '.0000000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'no_korean_file', 'N/A', '.0000000', 'UTF8', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'no_korean_file', 'N/A', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'no_korean_file', 'N/A', '.0000000', 'UTF8', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])
    
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'CP949', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'CP949', 'folder_with_header', 'N/A', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'CP949', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_compress'].append(["N/A", 'korean_file', 'N/A', '.0000000', 'CP949', 'folder_with_header', 'no_double_zipping', 'alphabetical_order'])

        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'folder_without_header', 'N/A', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'folder_without_header', 'N/A', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'no_double_zipping', 'folder_without_header', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'no_double_zipping', 'folder_without_header', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'double_zipping', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'double_zipping', 'folder_without_header', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'korean_file', '0x0A00', '.0000000', 'UTF8', 'double_zipping', 'folder_without_header', 'alphabetical_order'])
    
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'N/A', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'N/A', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'folder_without_header', 'N/A', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'folder_without_header', 'N/A', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'no_double_zipping', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'no_double_zipping', 'folder_without_header', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'no_double_zipping', 'folder_without_header', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'double_zipping', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', 'UTF8', 'N/A', 'double_zipping', 'alphabetical_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', '.0000000', '.0000000', 'UTF8', 'double_zipping', 'folder_without_header', 'different_order'])
        self.program['windows_alzip'].append(["N/A", 'no_korean_file', '0x0A00', 'UTF8', 'double_zipping', 'folder_without_header', 'alphabetical_order'])

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
            return "N/A"

