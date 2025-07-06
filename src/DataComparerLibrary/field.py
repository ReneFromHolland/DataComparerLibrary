import fnmatch
import re

from DataComparerLibrary.datetimehandler import DatetimeHandler
from DataComparerLibrary.matchstatus import MatchStatus
from DataComparerLibrary.report import Report
from DataComparerLibrary.tools import Tools


class Field:
    def __init__(self, field_data, row_nr, column_nr):
        self.field_data = field_data
        self.row_nr = row_nr
        self.column_nr = column_nr


    def equals(self, other_field_including_templates_and_literals, template_literals_dict):
        if self.field_data == other_field_including_templates_and_literals.field_data:
            return True

        # Replace literal templates with fixed external strings.
        other_field_data_including_templates = self.__replace_template_literals_dict(other_field_including_templates_and_literals.field_data, template_literals_dict)

        if self.field_data == other_field_data_including_templates:
            return True

        # Verify if difference is just a matter of difference in variable type.
        if Field.__is_same_value_but_different_types(self, other_field_data_including_templates):
            return False

        if isinstance(other_field_data_including_templates, int) or isinstance(other_field_data_including_templates, float):
            # A real integer or float, so templates are out of scope.
            Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "There is a difference between actual and expected data. No match with literals or templates.")
            return False

        # Check if data in actual match exact with template in expected data.
        # 0 = mismatch, 1 = match, 2 = non-match
        match_status = Field.__match_data_with_template_keyword(self, other_field_data_including_templates)
        #
        if match_status == MatchStatus.MISMATCH:
            return False
        elif match_status == MatchStatus.MATCH:
            return True

        equal = Field.__match_data_with_template(self, other_field_data_including_templates)
        #
        return equal


    @staticmethod
    def __replace_template_literals_dict(data, template_literals_dict):
        if template_literals_dict:
            for i in range(0, len(template_literals_dict)):
                data = data.replace(list(template_literals_dict.keys())[i], str(list(template_literals_dict.values())[i]))
        return data


    def __is_same_value_but_different_types(self, other_field_data):
        # Verify if difference is just a matter of difference in float, integer or string representation.
        if str(self.field_data) == str(other_field_data):
            type_field_data = Tools.get_full_typename(self.field_data)
            type_other_field_data = Tools.get_full_typename(other_field_data)
            Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data, "There is a difference between actual and expected data. Actual data is a(n) " +  type_field_data + " while expected data is a(n) " + type_other_field_data + ".")
            return True
        return False


    def __match_data_with_template_keyword(self, other_field_data_including_templates):
        match_status = MatchStatus.MATCH
        #
        match other_field_data_including_templates.upper():
            case "{PRESENT}":
                if not self.field_data:
                    # No data is present in actual data field.
                    match_status = MatchStatus.MISMATCH
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "Actual data field is not PRESENT")
            #
            case "{EMPTY}":
                if self.field_data:
                    # Actual data field is not empty.
                    match_status = MatchStatus.MISMATCH
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "Actual data field is not EMPTY")
            #
            case "{INTEGER}":
                if isinstance(self.field_data, int):
                    # A real integer (positive or negative).
                    match_status = MatchStatus.MATCH
                #
                elif self.field_data.isdigit():
                    # Test on INTEGER temporary less tide again
                    # Positive integer field in string format.
                    match_status = MatchStatus.MATCH
#                   Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "There is a difference between actual and expected data. Actual data is an INTEGER in string format while an INTEGER is expected.")
                elif isinstance(self.field_data, str):
                    match_status = MatchStatus.MISMATCH
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "There is a difference between actual and expected data. Actual data is a string while an INTEGER is expected.")
                else:
                    match_status = MatchStatus.MISMATCH
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "There is a difference between actual and expected data. Actual data field is not INTEGER.")
            #
            case "{SKIP}":
                match_status = MatchStatus.MATCH
            #
            case _:
                match_status = MatchStatus.NON_MATCH
        #
        return match_status


    def __match_data_with_template(self, other_field_data_including_templates):
        equal = True

        expected_data_including_date_template = None
        expected_data_with_wildcard = None
        skip_exception_rule_used = False

        if "{SKIP}" in other_field_data_including_templates.upper() or "{DATETIME_FORMAT():YYYYMMDDHHMMSSFF6}" in other_field_data_including_templates.upper():
            # Part(s) of the actual data field will be skipped for verification.
            # Replace {SKIP}, ignoring cases, by wildcard *.
            # compiled = re.compile(re.escape("{SKIP}"), re.IGNORECASE)
            # expected_data_with_wildcard = compiled.sub("*", other_field_data_including_templates)
            compiled = re.compile(re.escape("{SKIP}"), re.IGNORECASE)
            compiled2 = re.compile(re.escape("{DATETIME_FORMAT():YYYYMMDDHHMMSSFF6}"), re.IGNORECASE)
            expected_data_with_wildcard = compiled2.sub("*", compiled.sub("*", other_field_data_including_templates))
            #
            if fnmatch.fnmatch(self.field_data, expected_data_with_wildcard):
                skip_exception_rule_used = True
        #
        if expected_data_with_wildcard == None:
            # Wildcards not used.
            expected_data_including_date_template = other_field_data_including_templates
        else:
            expected_data_including_date_template = expected_data_with_wildcard
        #
        if "{NOW()" in other_field_data_including_templates.upper():
            matches = ["{NOW():", "{NOW()+", "{NOW()-"]
            if all([x not in other_field_data_including_templates.upper() for x in matches]):
                equal = False
                Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "NOW() has been found in expected data field, but format is incorrect.")
                #continue
            #
            expected_data = DatetimeHandler.replace_date_template_in_expected_data(self, expected_data_including_date_template)
            #
            if expected_data == -1:
                equal = False
                Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "NOW() has been found in expected data field, but format is incorrect.")
            else:
                if not fnmatch.fnmatch(self.field_data, expected_data):
                    # No match despite using of wildcard(s).
                    equal = False
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "Date template format displayed. See also next message line.")
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, expected_data, "There is a difference between actual and expected data.")
            # continue
            #
        elif "{NOT(" in other_field_data_including_templates.upper():
            try:
                unwanted_expected_data = Field.__get_unwanted_expected_data(expected_data_including_date_template)
                #
                if self.field_data == unwanted_expected_data:
                    # Unwanted match.
                    equal = False
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "NOT() template format displayed. See also next message line.")
                    Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, unwanted_expected_data, "Actual and expected data are equal. However actual data should NOT be equal to the expected data!!!")
            except Exception as exception_message:
                # print(f"An exception occurred: {exception_message}")
                equal = False
                Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "NOT() has been found in expected data field, but format is incorrect.")
            #
        else:
            if not skip_exception_rule_used:
                # No exceptions.
                equal = False
                Report.show_differences_comparation_result(self.row_nr, self.column_nr, self.field_data, other_field_data_including_templates, "There is a difference between actual and expected data. No exception rule has been used.")
        #
        return equal


    @staticmethod
    def __get_unwanted_expected_data(expected_data_field_including_date_template):
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
        if Tools.is_integer(unwanted_expected_data):
            unwanted_expected_data = int(unwanted_expected_data)
        return unwanted_expected_data


