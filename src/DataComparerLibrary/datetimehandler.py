import datetime
import dateutil.relativedelta
import re

class DatetimeHandler:
    def replace_date_template_in_expected_data(self, expected_data_field_including_date_template):
        # Replace date_template in expected data.
        # For example: This is text {NOW()-5Y2M1D:YYYY-MM-DD} and also text.  =>  This is text 2018-05-03 and also text.
        position_open_brace_today_text  = expected_data_field_including_date_template.find("{NOW()")
        position_close_brace_today_text = expected_data_field_including_date_template.find("}", position_open_brace_today_text)
        #
        if position_open_brace_today_text == -1:
            raise Exception("Open brace '{NOW()' not found.")
        #
        if position_close_brace_today_text == -1:
            raise Exception("Close brace '}' not found.")
        #
        expected_datetime_template_string = expected_data_field_including_date_template[position_open_brace_today_text:position_close_brace_today_text + 1]
        expected_datetime_string = DatetimeHandler.__convert_datetime_template_to_datetime(self, expected_datetime_template_string)
        #
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
                    relative_datetime = DatetimeHandler.__convert_relative_datetime_template_to_relative_datetime(self, relative_datetime_template_string[1:len(relative_datetime_template_string)])
                    #
                    match relative_datetime_template_string[0]:
                        case "+":
                            expected_datetime = datetime.datetime.now() + relative_datetime
                        case "-":
                            expected_datetime = datetime.datetime.now() - relative_datetime
                        case _:
                            raise Exception("'+' or '-' sign not found in '{NOW() relative datetime template string'.")
            case _:
                raise Exception("Datetime template format in {NOW() datetime string is incorrect. Split sign ':' to separate expectation and format has been found more than once.")
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
            raise Exception("Relative datetime template format in '{NOW() datetime template string' " + relative_datetime_str + " is incorrect.")

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
            raise Exception("Relative datetime template format in '{NOW() datetime template string' " + relative_datetime_str + " is incorrect.")
