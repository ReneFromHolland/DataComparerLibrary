import fnmatch
import re

from DataComparerLibrary.datetimehandler import DatetimeHandler
from DataComparerLibrary.report import Report
from DataComparerLibrary.tools import Tools

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

        number_of_rows = max(number_of_rows_actual_data, number_of_rows_expected_data)

        Report.show_2d_array(self, "Actual data", actual_data, 20)
        Report.show_2d_array(self, "Expected data", expected_data_including_templates, 20)

        Report().show_header_differences_actual_and_expected_data()

        for row_nr in range(number_of_rows):
            if row_nr >= number_of_rows_actual_data:
                difference_found = True
                if len(expected_data_including_templates[row_nr]) == 0:
                    Report.show_differences_comparation_result(self, row_nr, 0, "", "", "Row actual data is not PRESENT. Row expected data is EMPTY.")
                else:
                    Report.show_differences_comparation_result(self, row_nr, 0, "", expected_data_including_templates[row_nr][0], "Row actual data is not PRESENT.")
                continue
            #
            if row_nr >= number_of_rows_expected_data:
                difference_found = True
                if len(actual_data[row_nr]) == 0:
                    Report.show_differences_comparation_result(self, row_nr, 0, "", "", "Row actual data is EMPTY. Row expected data is not PRESENT.")
                else:
                    Report.show_differences_comparation_result(self, row_nr, 0, actual_data[row_nr][0], "", "Row expected data is not PRESENT.")
                continue
            #
            number_of_columns_actual_data   = len(actual_data[row_nr])
            number_of_columns_expected_data = len(expected_data_including_templates[row_nr])

            number_of_columns = max(number_of_columns_actual_data, number_of_columns_expected_data)

            for column_nr in range(number_of_columns):
                expected_data_including_date_template = None
                expected_data_with_wildcard = None
                skip_exception_rule_used = False
                #
                if column_nr >= number_of_columns_actual_data:
                    difference_found = True
                    Report.show_differences_comparation_result(self, row_nr, column_nr, "", expected_data_including_templates[row_nr][column_nr], "Column actual data is not PRESENT.")
                    continue
                #
                if column_nr >= number_of_columns_expected_data:
                    difference_found = True
                    Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], "", "Column expected data is not PRESENT.")
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
                            Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. Actual data is an integer while expected data is a string.")
                        elif isinstance(actual_data[row_nr][column_nr], str) and isinstance(expected_data_including_templates[row_nr][column_nr], int):
                            difference_found = True
                            Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. Actual data is a string while expected data is an integer.")
                        continue
                    #
                    # If data in actual and expected field doesn't match, check if a template has been used in expected data.
                    match expected_data_including_templates[row_nr][column_nr].upper():
                        case "{PRESENT}":
                            if not actual_data[row_nr][column_nr]:
                                # No data is present in actual data field.
                                difference_found = True
                                Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not PRESENT")
                        #
                        case "{EMPTY}":
                            if actual_data[row_nr][column_nr]:
                                # Actual data field is not empty.
                                difference_found = True
                                Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not EMPTY")
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
                                Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Actual data field is not INTEGER.")
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
                                    Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOW() has been found in expected data field, but format is incorrect.")
                                    continue
                                #
                                expected_data = DatetimeHandler.replace_date_template_in_expected_data(self, expected_data_including_date_template)
                                #
                                if expected_data == -1:
                                    difference_found = True
                                    Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOW() has been found in expected data field, but format is incorrect.")
                                else:
                                    if not fnmatch.fnmatch(actual_data[row_nr][column_nr], expected_data):
                                        # No match despite using of wildcard(s).
                                        difference_found = True
                                        Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "Date template format displayed. See also next message line.")
                                        Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data, "There is a difference between actual and expected data.")
                                continue
                                #
                            elif "{NOT(" in expected_data_including_templates[row_nr][column_nr].upper():
                                try:
                                    unwanted_expected_data = ArrayComparer.__get_unwanted_expected_data(self, expected_data_including_date_template)
                                    #
                                    if actual_data[row_nr][column_nr] == unwanted_expected_data:
                                        # Unwanted match.
                                        difference_found = True
                                        Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOT() template format displayed. See also next message line.")
                                        Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], unwanted_expected_data, "Actual and expected data are equal. However actual data should NOT be equal to the expected data!!!")
                                except Exception as exception_message:
                                    # print(f"An exception occurred: {exception_message}")
                                    difference_found = True
                                    Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "NOT() has been found in expected data field, but format is incorrect.")
                                #
                            else:
                                if not skip_exception_rule_used:
                                    # No exceptions.
                                    difference_found = True
                                    Report.show_differences_comparation_result(self, row_nr, column_nr, actual_data[row_nr][column_nr], expected_data_including_templates[row_nr][column_nr], "There is a difference between actual and expected data. No exception rule has been used.")
                            #
        if difference_found:
            print("\n\n\n")
            raise Exception("There is a difference between actual and expected data. See detail information.")
        else:
            print("There are no differences between actual and expected data found.")
            print("\n\n\n")

        #Report().show_footer_comparation_result()


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
        if Tools.is_integer(self, unwanted_expected_data):
            unwanted_expected_data = int(unwanted_expected_data)
        return unwanted_expected_data

