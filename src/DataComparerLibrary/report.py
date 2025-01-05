class Report:
    def show_header_and_data(self, header, data):
        Report.__show_2d_array(self, header, data, 20)


    def show_header_differences_actual_and_expected_data(self):
        print()
        print("=== Overview differences between actual and expected data")
        print()


#show_difference_between_actual_and_expected_data
    def show_differences_comparation_result(self, row_number, column_number, actual_data, expected_data, error_message):
        print("Row: ", row_number + 1, "  Column: ", column_number + 1, "  =>  Actual data: ", actual_data, "    Expected data: ", expected_data, "    Remark / Error message: ", error_message)


    #def show_footer(self, StatusMessage().difference):
    def show_footer_comparation_result(self):
        if StatusMessage().difference:
            print("\n\n\n")
            raise Exception("There is a difference between actual and expected data. See detail information.")
        else:
            print("There are no differences between actual and expected data found.")
            print("\n\n\n")


    def __show_2d_array(self, title, reader_file_list, column_width):
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