from DataComparerLibrary.row import Row
from DataComparerLibrary.report import Report


class TwoDArray:
    def __init__(self, two_d_array_data):
        self.two_d_array_data = two_d_array_data
        self.number_of_rows = len(two_d_array_data)


    def equals(self, other_two_d_array, template_literals_dict):
        equal = True
        #
        max_number_of_rows = max(self.number_of_rows, other_two_d_array.number_of_rows)
        #
        for row_nr in range(max_number_of_rows):
            if row_nr >= self.number_of_rows:
                equal = False
                if len(other_two_d_array.two_d_array_data[row_nr]) == 0:
                    Report.show_differences_comparation_result(row_nr, 0, "", "", "Row actual data is not PRESENT. Row expected data is EMPTY.")
                else:
                    Report.show_differences_comparation_result(row_nr, 0, "", other_two_d_array.two_d_array_data[row_nr][0], "Row actual data is not PRESENT.")
            #
            elif row_nr >= other_two_d_array.number_of_rows:
                equal = False
                if len(self.two_d_array_data[row_nr]) == 0:
                    Report.show_differences_comparation_result(row_nr, 0, "", "", "Row actual data is EMPTY. Row expected data is not PRESENT.")
                else:
                    Report.show_differences_comparation_result(row_nr, 0, self.two_d_array_data[row_nr][0], "", "Row expected data is not PRESENT.")
            #
            elif not Row(self.two_d_array_data[row_nr], row_nr).equals(Row(other_two_d_array.two_d_array_data[row_nr], row_nr), template_literals_dict):
                equal = False
            #
        return equal