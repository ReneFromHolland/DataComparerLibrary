# Script for comparing actual data with expected data.
#
import datetime
import fnmatch
import re
import dateutil.relativedelta


class ArrayComparer:
    def compare_data(self, actual_data, expected_data_including_templates, template_literals_dict):
        difference_found = False
        #
        if actual_data and type(actual_data[0]) is not list:  # only a single row
            actual_data = [actual_data,]  # add row to tuple of lenght 1
        #
        if expected_data_including_templates and type(expected_data_including_templates[0]) is not list:  # only a single row
            expected_data_including_templates = [expected_data_including_templates,]  # add row to tuple of lenght 1

        number_of_rows_actual_data = len(actual_data)
        number_of_rows_expected_data = len(expected_data_including_templates)

        number_of_rows = number_of_rows_actual_data if (number_of_rows_actual_data >= number_of_rows_expected_data) else number_of_rows_expected_data

        ArrayComparer.__print_2d_array(self, "Actual data", actual_data, 20)
        ArrayComparer.__print_2d_array(self, "Expected data", expected_data_including_templates, 20)

        print()
        print("=== Overview differences between actual and expected data")
        print()

        for row_nr in range(number_of_rows):
            if row_nr >= number_of_rows_actual_data:
                difference_found = True
                if len(expected_data_including_templates[row_nr]) == 0:
                    ArrayComparer.__print_comparation_result(self, row_nr, 0, "", "", "Row actual data is not PRESENT. Row expected data is EMPTY.")
                else:
                    ArrayComparer.__print_comparation_result(self, row_nr, 0, "", expected_data_including_templates[row_nr][0], "Row actual data is not PRESENT.")
                continue
            #
            if row_nr >= number_of_rows_expected_data:
                difference_found = True
                if len(actual_data[row_nr]) == 0:
                    ArrayComparer.__print_comparation_result(self, row_nr, 0, "", "", "Row actual data is EMPTY. Row expected data is not PRESENT.")
                else:
                    ArrayComparer.__print_comparation_result(self, row_nr, 0, actual_data[row_nr][0], "", "Row expected data is not PRESENT.")
                continue
            #
            number_of_columns_actual_data   = len(actual_data[row_nr])
            number_of_columns_expected_data = len(expected_data_including_templates[row_nr])

            number_of_columns = number_of_columns_actual_data if (number_of_columns_actual_data >= number_of_columns_expected_data) else number_of_columns_expected_data

            for column_nr in range(number_of_columns):
                expected_data_including_date_template = None
                expected_data_with_wildcard = None
                skip_exception_rule_used = False
                #
                if column_nr >= number_of_columns_actual_data:
                    difference_found = True
                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, "", expected_data_including_templates[row_nr][column_nr], "Column actual data is not PRESENT.")
                    continue
                #
                if column_nr >= number_of_columns_expected_data:
                    difference_found = True
                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], "", "Column expected data is not PRESENT.")
                    continue
                #
                if actual_data[row_nr][column_nr] != expected_data_including_templates[row_nr][column_nr]:
                    # Replace literal templates with fixed external strings.
                    if template_literals_dict:
                        for i in range(0, len(template_literals_dict)):
#                           key = list(template_literals_dict.keys())[i]
#                           value = list(template_literals_dict.values())[i]
#                           print("key: ", key)
#                           print("value: ", value)
                            expected_data_including_templates[row_nr][column_nr] = expected_data_including_templates[row_nr][column_nr].replace(list(template_literals_dict.keys())[i], list(template_literals_dict.values())[i])
#                           print("actual_data[row_nr][column_nr]: \n", actual_data[row_nr][column_nr])
#                           print("expected_data_including_templates[row_nr][column_nr]: \n", expected_data_including_templates[row_nr][column_nr])


                    # Verify if difference is a matter of string versus integer representation.
                    if str(actual_data[row_nr][column_nr]) == str(expected_data_including_templates[row_nr][column_nr]):
                        if isinstance(actual_data[row_nr][column_nr], int) and isinstance(expected_data_including_templates[row_nr][column_nr], str):
                            difference_found = True
                            ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. Actual data is an integer while expected data is a string.")
                        elif isinstance(actual_data[row_nr][column_nr], str) and isinstance(expected_data_including_templates[row_nr][column_nr], int):
                            difference_found = True
                            ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. Actual data is a string while expected data is an integer.")
                        continue
                    #
                    # If data in actual and expected field doesn't match, check if a template has been used in expected data.
                    match expected_data_including_templates[row_nr][column_nr].upper():
                        case "{PRESENT}":
                            if not actual_data[row_nr][column_nr]:
                                # No data is present in actual data field.
                                difference_found = True
                                ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not PRESENT")
                        #
                        case "{EMPTY}":
                            if actual_data[row_nr][column_nr]:
                                # Actual data field is not empty.
                                difference_found = True
                                ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not EMPTY")
                        #
                        case "{INTEGER}":
                            if isinstance(actual_data[row_nr][column_nr], int):
                                # A real integer.
                                continue
                            #
                            # Verify if string is integer.
                            if not actual_data[row_nr][column_nr].isdigit():
                                # Not positive integer field.
                                difference_found = True
                                ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not INTEGER.")
                        #
                        case "{SKIP}":
                            pass
                        case _:
                            if "{SKIP}" in expected_data_including_templates[row_nr][column_nr].upper() or "{DATETIME_FORMAT():YYYYMMDDHHMMSSFF6}" in expected_data_including_templates[row_nr][column_nr].upper():
                                if expected_data_including_templates[row_nr][column_nr].upper() == "{SKIP}":
                                    # Complete actual data field will be skipped for verification.
                                    pass
                                else:
                                    # Part(s) of the actual data field will be skipped for verification.
                                    # Replace {SKIP}, ignoring cases, by wildcard *.
                                    # compiled = re.compile(re.escape("{SKIP}"), re.IGNORECASE)
                                    # expected_data_with_wildcard = compiled.sub("*", expected_data_including_templates[row_nr][column_nr])
                                    compiled = re.compile(re.escape("{SKIP}"), re.IGNORECASE)
                                    compiled2 = re.compile(re.escape("{DATETIME_FORMAT():YYYYMMDDHHMMSSFF6}"), re.IGNORECASE)
                                    expected_data_with_wildcard = compiled2.sub("*", compiled.sub("*", expected_data_including_templates[row_nr][column_nr]))
                                    #
                                    if fnmatch.fnmatch(actual_data[row_nr][column_nr], expected_data_with_wildcard):
                                        skip_exception_rule_used = True
                                        continue
                            #
                            if expected_data_with_wildcard is None:
                                # Wildcards not used.
                                expected_data_including_date_template = expected_data_including_templates[row_nr][column_nr]
                            else:
                                expected_data_including_date_template = expected_data_with_wildcard
                            #
                            if "{NOW()" in expected_data_including_templates[row_nr][column_nr].upper():
                                matches = ["{NOW():", "{NOW()+", "{NOW()-"]
                                if all([x not in expected_data_including_templates[row_nr][column_nr].upper() for x in matches]):
                                    difference_found = True
                                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOW() has been found in expected data field, but format is incorrect.")
                                    continue
                                #
                                expected_data = ArrayComparer.__replace_date_template_in_expected_data(self, expected_data_including_date_template)
                                #
                                if expected_data == -1:
                                    difference_found = True
                                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOW() has been found in expected data field, but format is incorrect.")
                                else:
                                    if not fnmatch.fnmatch(actual_data[row_nr][column_nr], expected_data):
                                        # No match despite using of wildcard(s).
                                        difference_found = True
                                        ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Date template format displayed. See also next message line.")
                                        ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data, "There is a difference between actual and expected data.")
                                continue
                                #
                            elif "{NOT(" in expected_data_including_templates[row_nr][column_nr].upper():
                                try:
                                    unwanted_expected_data = ArrayComparer.__get_unwanted_expected_data(self, expected_data_including_date_template)
                                    #
                                    if actual_data[row_nr][column_nr] == unwanted_expected_data:
                                        # Unwanted match.
                                        difference_found = True
                                        ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOT() template format displayed. See also next message line.")
                                        ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], unwanted_expected_data, "Actual and expected data are equal. However actual data should NOT be equal to the expected data!!!")
                                except Exception as exception_message:
                                    # print(f"An exception occurred: {exception_message}")
                                    difference_found = True
                                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOT() has been found in expected data field, but format is incorrect.")
                                #
                            else:
                                if not skip_exception_rule_used:
                                    # No exceptions.
                                    difference_found = True
                                    ArrayComparer.__print_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. No exception rule has been used.")
                            #
        if difference_found:
            print("\n\n\n")
            raise Exception("There is a difference between actual and expected data. See detail information.")
        else:
            print("There are no differences between actual and expected data found.")
            print("\n\n\n")


    def __replace_date_template_in_expected_data(self, expected_data_field_including_date_template):
        # Replace date_template in expected data.
        # For example: This is text {NOW()-5Y2M1D:YYYY-MM-DD} and also text.  =>  This is text 2018-05-03 and also text.
        position_open_brace_today_text  = expected_data_field_including_date_template.find("{NOW()")
        position_close_brace_today_text = expected_data_field_including_date_template.find("}", position_open_brace_today_text)
        #
        if position_close_brace_today_text == -1:
            return -1
        # Close brace of TODAY has been found.
        #
        expected_datetime_template_string = expected_data_field_including_date_template[position_open_brace_today_text:position_close_brace_today_text + 1]
        expected_datetime_string = ArrayComparer.__convert_datetime_template_to_datetime(self, expected_datetime_template_string)
        #
        if expected_datetime_string == -1:
            return -1
        # Datetime_template_string has been converted to datetime.
        #
        # Replace expected_datetime_template_string by expected_datetime_string in expected_data_field_including_template.
        compiled = re.compile(re.escape(expected_datetime_template_string), re.IGNORECASE)
        expected_data_with_calculated_date = compiled.sub(expected_datetime_string, expected_data_field_including_date_template)
        #
        return expected_data_with_calculated_date


    def __convert_datetime_template_to_datetime(self, expected_datetime_format):
        # Convert expected datetime template into datetime.
        # For example: {NOW():YYYY-MM-DD}         =>  2023-07-04
        #              {NOW():MMDDYY}             =>  070423
        #              {NOW()-5Y3M1D:D-MMMM-YY}   =>  3-April-18
        #              {NOW()-5Y2M1D:YYYY-MMM-DD} =>  2018-Apr-03
        #              {NOW()-5Y2M1D:YYYYMMDD}    =>  20180503
        #              {NOW()-5Y2M1D:YYYY-M-D}    =>  2018-5-3
        #              {NOW()+2D:DDMMYYYY         =>  06072023
        #              {NOW()-5Y2M1D:YYYY-MM-DD}  =>  2018-05-03
        template_datetime_string_splitted = expected_datetime_format.split(":")
        #
        match len(template_datetime_string_splitted):
            case 2:
                if template_datetime_string_splitted[0] == "{NOW()":
                    # Current date time.
                    expected_datetime = datetime.datetime.now()
                else:
                    # Adjust date time based on current date time.
                    relative_datetime_template_string = template_datetime_string_splitted[0].replace('{NOW()', '')
                    relative_datetime = ArrayComparer.__convert_relative_datetime_template_to_relative_datetime(self, relative_datetime_template_string[1:len(relative_datetime_template_string)])
                    if relative_datetime == -1:
                        return -1
                    else:
                        match relative_datetime_template_string[0]:
                            case "+":
                                expected_datetime = datetime.datetime.now() + relative_datetime
                            case "-":
                                expected_datetime = datetime.datetime.now() - relative_datetime
                            case _:
                                return -1
            case _:
                return -1
        #
        year = expected_datetime.strftime("%Y")
        year_2_digits = expected_datetime.strftime("%y")
        month = expected_datetime.strftime("%m")
        month_abbreviated = expected_datetime.strftime("%b")
        month_full = expected_datetime.strftime("%B")
        day = expected_datetime.strftime("%d")
        #
        expected_date = template_datetime_string_splitted[1][0:len(template_datetime_string_splitted[1]) - 1].replace("YYYY", year).replace("YY", year_2_digits).replace("MMMM", month_full).replace("MMM", month_abbreviated).replace("MM", month).replace("M", month.lstrip("0")).replace("DD", day).replace("D", day.lstrip("0"))
        return expected_date


    def __convert_relative_datetime_template_to_relative_datetime(self, relative_datetime_str):
        # Convert relative datetime template to relative datetime.
        # For example: 2Y5M1D  =>  2 years, 5 months, 1 day   (used to add to or subtract from current moment / date)
        # \d+ means 1 of more digits; search on character - for example Y;
        regex = re.compile(r'((?P<years>\d+?)Y)?((?P<months>\d+?)M)?((?P<days>\d+?)D)?((?P<hours>\d+?)h)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?')
        period = regex.match(relative_datetime_str)

        if not period:
            return -1

        period = period.groupdict()
        kwargs = {}
        period_names = ["years", "months", "days"]
        #
        for name, param in period.items():
            if param:
                period_name = name
                period_count = param
                #
                if period_name in period_names:
                    kwargs[period_name] = int(period_count)
        #
        if kwargs:
            return dateutil.relativedelta.relativedelta(**kwargs)
        else:
            return -1


    def __print_2d_array(self, title, reader_file_list, column_width):
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


    def __print_comparation_result(self, row_number, column_number, actual_data, expected_data, error_message):
        print("Row: ", row_number + 1, "  Column: ", column_number + 1, "  =>  Actual data: ", actual_data, "    Expected data: ", expected_data, "    Remark / Error message: ", error_message)


    def __get_unwanted_expected_data(self, expected_data_field_including_date_template):
        position_open_brace = expected_data_field_including_date_template.find("{NOT(")
        position_close_brace = expected_data_field_including_date_template.find(")}", position_open_brace)
        #
        if position_open_brace == -1:
            #print("position_open_brace:", position_open_brace)
            raise Exception()
        #
        if position_close_brace == -1:
            #print("position_close_brace:", position_close_brace)
            raise Exception()
        #
        unwanted_expected_data = expected_data_field_including_date_template[position_open_brace+5:position_close_brace]
        #
        if ArrayComparer.is_integer(self, unwanted_expected_data):
            unwanted_expected_data = int(unwanted_expected_data)
        return unwanted_expected_data



    def is_integer(self, string):
        if string[0] == '-':
            # if a negative number
            return string[1:].isdigit()
        else:
            return string.isdigit()


