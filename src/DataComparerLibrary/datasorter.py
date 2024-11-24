# Script for sorting an input file. Sorted result will be written to an output file. Encoding is UFT-08.
#
import csv
import os
from DataComparerLibrary.delimitertranslator import DelimiterTranslator


class DataSorter:
    def sort_csv_file(self, input_file, output_file, number_of_header_lines=0, number_of_trailer_lines=0, sort_on_columns_list=None, delimiter=',', quotechar=None):
        try:
            if not os.path.isfile(input_file):
                raise Exception("Input file doesn't exists: ", input_file)
            #
            print("input_file: ", input_file)
            print("output_file: ", output_file)
            print("number_of_header_lines: ", number_of_header_lines)
            print("number_of_trailer_lines: ", number_of_trailer_lines)
            print("sort_on_columns_list: ", sort_on_columns_list)
            print("delimiter: ", delimiter)
            print("quotechar: ", quotechar)
            #
            number_of_records_input_file = 0
            with open(input_file) as input_file_row_count:
                number_of_records_input_file = sum(1 for line in input_file_row_count)
            #
            print("number_of_records_input_file: ", number_of_records_input_file)
            #
            number_of_header_lines = int(number_of_header_lines)
            number_of_trailer_lines = int(number_of_trailer_lines)
            #
            if number_of_records_input_file < number_of_header_lines + number_of_trailer_lines:
                raise Exception("The number of records in the input file is less than the declared number of header and trailer lines.")
            #
            number_of_sort_columns = 0
            if sort_on_columns_list:
                number_of_sort_columns = len(sort_on_columns_list)
            print("number_of_sort_columns: ", number_of_sort_columns)
            #
            with open(input_file, mode='rt', encoding='utf-8') as input_file, open(output_file, mode='w', newline='', encoding='utf-8') as output_file:
                if len(delimiter) == 1:
                    input_data = list(csv.reader(input_file, delimiter=delimiter, quotechar=quotechar))
                    output_data = csv.writer(output_file, delimiter=delimiter, quotechar=quotechar)
                else:
                    input_data = list(csv.reader((line.replace(delimiter, chr(255)) for line in input_file), delimiter=chr(255), quotechar=quotechar))
                    translator = DelimiterTranslator(output_file, chr(255), delimiter)
                    output_data = csv.writer(translator, delimiter=chr(255), quotechar=quotechar)
                #
                data_text = []
                trailer_text = []
                #
                if number_of_header_lines == 0 and number_of_trailer_lines == 0:
                    # Only data lines.
                    data_text = input_data
                else:
                    # Header or/and trailer or/and data lines present.
                    line_nr = 0
                    #
                    # Separate in header, data and trailer text.
                    for row in input_data:
                        line_nr += 1
                        if number_of_header_lines != 0 and line_nr <= number_of_header_lines:
                            # A header line.
                            output_data.writerow(row)
                        elif number_of_trailer_lines != 0 and line_nr > number_of_records_input_file - number_of_trailer_lines:
                            # A trailer line.
                            trailer_text.append(row)
                        else:
                            # A data line.
                            data_text.append(row)
                #
                sorted_data_text = DataSorter.__sort_data_records(self, data_text, sort_on_columns_list)
                #
                for row in sorted_data_text:
                    output_data.writerow(row)

                for row in trailer_text:
                    output_data.writerow(row)
            #
        except IndexError as error:
            raise Exception("Probably selected column doesn't exist. Correct argument 'sort_on_columns_list'. Error message: ", type(error).__name__, "–", error)
        except Exception as error:
            raise Exception("Error message: ", type(error).__name__, "–", error)



    def __sort_data_records(self, data_text, sort_on_columns_list):
        number_of_sort_columns = 0
        if sort_on_columns_list:
            number_of_sort_columns = len(sort_on_columns_list)
        print("number_of_sort_columns: ", number_of_sort_columns)
        #
        match number_of_sort_columns:
            case 0:
                sorted_data_text = sorted(data_text, key=lambda column: (column[0]))
            case 1:
                a = sort_on_columns_list[0]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)]))
            case 2:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)]))
            case 3:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                c = sort_on_columns_list[2]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)], int(column[c]) if isinstance(c, int) else column[int(c)]))
            case 4:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                c = sort_on_columns_list[2]
                d = sort_on_columns_list[3]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)], int(column[c]) if isinstance(c, int) else column[int(c)], int(column[d]) if isinstance(d, int) else column[int(d)]))
            case 5:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                c = sort_on_columns_list[2]
                d = sort_on_columns_list[3]
                e = sort_on_columns_list[4]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)], int(column[c]) if isinstance(c, int) else column[int(c)], int(column[d]) if isinstance(d, int) else column[int(d)], int(column[e]) if isinstance(e, int) else column[int(e)]))
            case 6:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                c = sort_on_columns_list[2]
                d = sort_on_columns_list[3]
                e = sort_on_columns_list[4]
                f = sort_on_columns_list[5]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)], int(column[c]) if isinstance(c, int) else column[int(c)], int(column[d]) if isinstance(d, int) else column[int(d)], int(column[e]) if isinstance(e, int) else column[int(e)], int(column[f]) if isinstance(f, int) else column[int(f)]))
            case 7:
                a = sort_on_columns_list[0]
                b = sort_on_columns_list[1]
                c = sort_on_columns_list[2]
                d = sort_on_columns_list[3]
                e = sort_on_columns_list[4]
                f = sort_on_columns_list[5]
                g = sort_on_columns_list[6]
                sorted_data_text = sorted(data_text, key=lambda column: (int(column[a]) if isinstance(a, int) else column[int(a)], int(column[b]) if isinstance(b, int) else column[int(b)], int(column[c]) if isinstance(c, int) else column[int(c)], int(column[d]) if isinstance(d, int) else column[int(d)], int(column[e]) if isinstance(e, int) else column[int(e)], int(column[f]) if isinstance(f, int) else column[int(f)], int(column[g]) if isinstance(g, int) else column[int(g)]))
            case _:
                raise Exception("Too many columns selected for sorting. Only sorting on maximum 7 columns is supported.")
        return sorted_data_text
