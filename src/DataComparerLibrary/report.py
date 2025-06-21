from DataComparerLibrary.tools import Tools

class Report:
    @staticmethod
    def show_version_of_program():
        print()
        print("=== DataComparerLibrary Version: ", Tools.get_version_of_program('DataComparerLibrary'), " ====")
        print()


    @staticmethod
    def show_header_and_data(header, data):
        Report.show_2d_array(header, data, 20)


    @staticmethod
    def show_header_differences_actual_and_expected_data():
        print()
        print("=== Overview differences between actual and expected data")
        print()


    #show_difference_between_actual_and_expected_data
    @staticmethod
    def show_differences_comparation_result(row_number, column_number, actual_data, expected_data, error_message):
        print("Row: ", row_number + 1, "  Column: ", column_number + 1, "  =>  Actual data: ", actual_data, "    Expected data: ", expected_data, "    Remark / Error message: ", error_message)


    @staticmethod
    def show_footer_comparation_result(equal):
        if equal:
            print("\n\n\n")
            print("There are no differences between actual and expected data found.")
            print("\n\n\n")
        else:
            print("\n\n\n")
            raise Exception("There is a difference between actual and expected data. See detail information.")



    @staticmethod
    def show_2d_array(title, reader_file_list, column_width):
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
                if isinstance(cell_value, float) or isinstance(cell_value, int) or isinstance(cell_value, str):
                    #print('{val:{fill}{width}}'.format(val=cell_value, fill='', width=column_width), end="  ")
                    print('{val:{fill}{width}}'.format(val=cell_value, fill='', width=column_width, left_aligned=True), end="  ")

            print()
        print()
        print()