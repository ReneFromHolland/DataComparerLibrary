# Script for conversion on an input file. The converted result will be written to an output file.
# The files are open in binary mode.
# Currently, methods are implemented to remove or replace a separate linefeed within a record. Records are ended by carriage return linefeed.
#
import csv
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

