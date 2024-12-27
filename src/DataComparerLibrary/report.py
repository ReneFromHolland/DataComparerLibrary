class Report:
    def show_2d_array(self, title, reader_file_list, column_width):
        max_length_title = 30
        title = title[0:(max_length_title - 1)]
        length_title = len(title)
        print("=== ", title, " ", end="")
        print("=" * (max_length_title - length_title))
        print()
        #
        for row in reader_file_list:
            for cell_value in row:
                #if isinstance(cell_value, str):
                if isinstance(cell_value, str) or isinstance(cell_value, int):
                    #print('{val:{fill}{width}}'.format(val=cell_value, fill='', width=column_width), end="  ")
                    print('{val:{fill}{width}}'.format(val=cell_value, fill='', width=column_width, left_aligned=True), end="  ")

            print()
        print()
        print()


    def show_comparation_result(self, row_number, column_number, actual_data, expected_data, error_message):
        print("Row: ", row_number + 1, "  Column: ", column_number + 1, "  =>  Actual data: ", actual_data, "    Expected data: ", expected_data, "    Remark / Error message: ", error_message)
