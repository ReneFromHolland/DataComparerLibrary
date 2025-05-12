from DataComparerLibrary.field import Field
from DataComparerLibrary.report import Report


class Row:
    def __init__(self, row_data, row_nr):
        self.row_data = row_data
        self.row_nr = row_nr
        #
        self.number_of_columns = len(row_data)


    def equals(self, other_row, template_literals_dict):
        equal = True
        #
        max_number_of_columns = max(self.number_of_columns, other_row.number_of_columns)
        #
        for column_nr in range(max_number_of_columns):
            if column_nr >= self.number_of_columns:
                equal = False
                Report.show_differences_comparation_result(self.row_nr, column_nr, "", other_row.row_data[column_nr], "Column actual data is not PRESENT.")
            #
            elif column_nr >= other_row.number_of_columns:
                equal = False
                Report.show_differences_comparation_result(self.row_nr, column_nr, self.row_data[column_nr], "", "Column expected data is not PRESENT.")
            #
            elif not Field(self.row_data[column_nr], self.row_nr, column_nr).equals(Field(other_row.row_data[column_nr], self.row_nr, column_nr), template_literals_dict):
                equal = False
            #
        return equal
