# Script for conversion on an input file. The converted result will be written to an output file.
# The files are open in binary mode.
# Currently, methods are implemented to remove or replace a separate linefeed within a record. Records are ended by carriage return linefeed.
#
import csv
import openpyxl
import os
import re
import warnings


class FileConverter:
    @staticmethod
    def remove_separate_lf(input_file, output_file):
        # Remove separate linefeed (LF), so carriage return linefeed (CRLF) remains.
        try:
            if not os.path.exists(input_file):
                raise Exception("Input file doesn't exists: ", input_file)
            #
            print("input_file: ", input_file)
            print("output_file: ", output_file)
            #
            with open(input_file, "rb") as input_file:
                with open(output_file, "wb") as output_file:
                    output_file.write(re.sub(b"(?<!\r)\n", b"", input_file.read()))
            #
        except Exception as error:
            raise Exception("Error message: ", type(error).__name__, "–", error)


    @staticmethod
    def replace_separate_lf(input_file, output_file, replacement_string, encoding_replacement_string='utf-8'):
        # Replace separate linefeed (LF), so carriage return linefeed (CRLF) remains.
        try:
            if not os.path.exists(input_file):
                raise Exception("Input file doesn't exists: ", input_file)
            #
            print("input_file: ", input_file)
            print("output_file: ", output_file)
            print("replacement_string: ", replacement_string)
            print("encoding: ", encoding_replacement_string)
            #
            with open(input_file, "rb") as input_file:
                with open(output_file, "wb") as output_file:
                    output_file.write(re.sub(b"(?<!\r)\n", replacement_string.encode(encoding_replacement_string), input_file.read()))
            #
        except Exception as error:
            raise Exception("Error message: ", type(error).__name__, "–", error)


    @staticmethod
    def remove_cr_and_lf(input):
        # Remove carriage return (CR) and linefeed (LF) from input string.
        print("input: ", input)
        output = str(input).replace("\r", "").replace("\n", "")
        print("output: ", output)
        #
        return output


    @staticmethod
    def replace_cr_and_lf(input, replacement_string):
        # Replace carriage return (CR) and linefeed (LF) from input string.
        print("input: ", input)
        output = str(input).replace("\r", replacement_string).replace("\n", replacement_string)
        print("output: ", output)
        #
        return output


    @staticmethod
    def convert_excel_file_to_csv_file(excel_file, csv_file):
        if not os.path.exists(excel_file):
            raise Exception("Input file doesn't exists: ", excel_file)

        if not excel_file.endswith('.xslx') and not excel_file.endswith('.xslm') and not excel_file.endswith('.xls') and not excel_file.endswith('.xlm'):
            raise Exception("Input file is not a Excel-file: ", excel_file)

        if not excel_file.endswith('.csv'):
            raise Exception("Input file is not a csv-file: ", csv_file)

        with warnings.catch_warnings():
             warnings.filterwarnings("ignore", message="Workbook contains no defaultstyle", category=UserWarning)
             #
             excel = openpyxl.load_workbook(excel_file)
             # select the active sheet
             sheet = excel.active
             #
             # write the data in a csv-file
             col = csv.writer(open(csv_file, 'w', newline=""))
             #
             for row in sheet.rows:
                col.writerow([cell.value for cell in row])
