# Script for comparing csv-files, 2d-array with a csv-file or 2d-arrays and for comparing text-files, text variable with a text-file or text variables.
#
import csv
import os

from DataComparerLibrary.twodarray import TwoDArray
from DataComparerLibrary.report import Report


class DataComparer:
    def compare_data_2d_array_with_file(self, actual_data, expected_file, delimiter_expected_data=",", quotechar_expected_data='"', template_literals_dict=None):
        self.__check_if_actual_data_is_present(actual_data)
        self.__check_if_expected_file_is_present(expected_file)
        #
        expected_data = self.__get_data_from_csv_input_file(expected_file, delimiter_expected_data, quotechar_expected_data)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_data_file_with_2d_array(self, actual_file, expected_data, delimiter_actual_data=",", quotechar_actual_data='"', template_literals_dict=None):
        self.__check_if_actual_file_is_present(actual_file)
        self.__check_if_expected_data_is_present(expected_data)
        #
        actual_data = self.__get_data_from_csv_input_file(actual_file, delimiter_actual_data, quotechar_actual_data)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_data_2d_arrays(self, actual_data, expected_data, template_literals_dict=None):
        self.__check_if_actual_data_is_present(actual_data)
        self.__check_if_expected_data_is_present(expected_data)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_data_files(self, actual_file, expected_file, delimiter_actual_data=",", delimiter_expected_data=",", quotechar_actual_data='"', quotechar_expected_data='"', template_literals_dict=None):
        self.__check_if_actual_file_is_present(actual_file)
        self.__check_if_expected_file_is_present(expected_file)
        #
        actual_data = self.__get_data_from_csv_input_file(actual_file, delimiter_actual_data, quotechar_actual_data)
        expected_data = self.__get_data_from_csv_input_file(expected_file, delimiter_expected_data, quotechar_expected_data)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)



    def compare_text_variable_with_text_file(self, actual_text, expected_file, template_literals_dict=None):
        self.__check_if_actual_data_is_present(actual_text)
        self.__check_if_expected_file_is_present(expected_file)
        #
        actual_data = self.__split_text_into_textline_array(actual_text)
        expected_data = self.__split_textfile_into_textline_array(expected_file)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_text_file_with_text_variable(self, actual_file, expected_text, template_literals_dict=None):
        self.__check_if_actual_file_is_present(actual_file)
        self.__check_if_expected_data_is_present(expected_text)
        #
        actual_data = self.__split_textfile_into_textline_array(actual_file)
        expected_data = self.__split_text_into_textline_array(expected_text)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_text_variables(self, actual_text, expected_text, template_literals_dict=None):
        self.__check_if_actual_data_is_present(actual_text)
        self.__check_if_expected_data_is_present(expected_text)
        #
        actual_data = self.__split_text_into_textline_array(actual_text)
        expected_data = self.__split_text_into_textline_array(expected_text)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)


    def compare_text_files(self, actual_file, expected_file, template_literals_dict=None):
        self.__check_if_actual_file_is_present(actual_file)
        self.__check_if_expected_file_is_present(expected_file)
        #
        actual_data = self.__split_textfile_into_textline_array(actual_file)
        expected_data = self.__split_textfile_into_textline_array(expected_file)
        #
        DataComparer.__compare_data(actual_data, expected_data, template_literals_dict)



    @staticmethod
    def __compare_data(actual_data, expected_data, template_literals_dict=None):
        if template_literals_dict is not None and not isinstance(template_literals_dict, dict):
            raise Exception(f"The argument passed to parameter 'template_literals_dict' is not a dictionary. Value is: '{template_literals_dict}'.")
        actual_data = DataComparer.__make_data_2d_compliant(actual_data)
        expected_data = DataComparer.__make_data_2d_compliant(expected_data)
        #
        Report.show_version_of_program()
        Report.show_header_and_data("Actual data", actual_data)
        Report.show_header_and_data("Expected data", expected_data)
        Report.show_header_differences_actual_and_expected_data()
        #
        Report().show_footer_comparation_result(TwoDArray(actual_data).equals(TwoDArray(expected_data), template_literals_dict))


    @staticmethod
    def __check_if_actual_data_is_present(data):
        if data == None:
            raise Exception("Actual Input data unknown.")


    @staticmethod
    def __check_if_expected_data_is_present(data):
        if data == None:
            raise Exception("Expected Input data unknown.")


    @staticmethod
    def __check_if_actual_file_is_present(file):
        if os.path.exists(file):
            print("actual_file: ", file)
        else:
            raise Exception("Actual Input file doesn't exists: ", file)


    @staticmethod
    def __check_if_expected_file_is_present(file):
        if os.path.exists(file):
            print("expected_file: ", file)
        else:
            raise Exception("Expected Input file doesn't exists: ", file)


    @staticmethod
    def __get_data_from_csv_input_file(input_file, delimiter_data=",", quotechar_data='"'):
        with open(input_file, mode='rt', encoding='utf-8') as input_file:
            if len(delimiter_data) == 1:
                data = list(csv.reader(input_file, delimiter=delimiter_data, quotechar=quotechar_data))
            else:
                data = list(csv.reader((line.replace(delimiter_data, chr(255)) for line in input_file), delimiter=chr(255), quotechar=quotechar_data))
        #
        return data


    @staticmethod
    def __split_text_into_textline_array(text):
        data = []
        for line in text.split('\n'):
            data.append(line.strip('\n').split(chr(255)))
        #
        return data


    @staticmethod
    def __split_textfile_into_textline_array(input_file):
        with open(input_file, mode='rt', encoding='utf-8') as input_file:
            data = []
            for line in input_file.readlines():
                data.append(line.strip('\n').split(chr(255)))
        #
        return data


    @staticmethod
    def __make_data_2d_compliant(data):
        if data and type(data[0]) is not list:  # only a single row
            data = [data,]  # add row to tuple of lenght 1
        return data
