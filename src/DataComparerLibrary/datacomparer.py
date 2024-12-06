# Script for comparing actual data from an output file or a SQL-query with expected data in a file.
#
import csv
import os

from DataComparerLibrary.arraycomparer import ArrayComparer


class DataComparer:
    def compare_data_2d_array_with_file(self, actual_data, expected_file, delimiter_expected_data=",", quotechar_expected_data='"', template_literals_dict=None):
        if 'actual_data' not in locals():
            raise Exception("Input Actual data unknown.")
        #
        if not os.path.exists(expected_file):
            raise Exception("Input file doesn't exists: ", expected_file)
        #
        print("expected_file: ", expected_file)
        #
        with open(expected_file, mode='rt', encoding='utf-8') as expected_file:
            if len(delimiter_expected_data) == 1:
                expected_data = list(csv.reader(expected_file, delimiter=delimiter_expected_data, quotechar=quotechar_expected_data))
            else:
                expected_data = list(csv.reader((line.replace(delimiter_expected_data, chr(255)) for line in expected_file), delimiter=chr(255), quotechar=quotechar_expected_data))
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_data_file_with_2d_array(self, actual_file, expected_data, delimiter_actual_data=",", quotechar_actual_data='"', template_literals_dict=None):
        if not os.path.exists(actual_file):
            raise Exception("Input file doesn't exists: ", actual_file)
        #
        if 'expected_data' not in locals():
            raise Exception("Input Expected data unknown.")
        #
        print("actual_file: ", actual_file)
        #
        with open(actual_file, mode='rt', encoding='utf-8') as actual_file:
            if len(delimiter_actual_data) == 1:
                actual_data = list(csv.reader(actual_file, delimiter=delimiter_actual_data, quotechar=quotechar_actual_data))
            else:
                actual_data = list(csv.reader((line.replace(delimiter_actual_data, chr(255)) for line in actual_file), delimiter=chr(255), quotechar=quotechar_actual_data))
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_data_2d_arrays(self, actual_data, expected_data, template_literals_dict=None):
        if 'actual_data' not in locals():
            raise Exception("Input Actual data unknown.")
        #
        if 'expected_data' not in locals():
            raise Exception("Input Expected data unknown.")
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_data_files(self, actual_file, expected_file, delimiter_actual_data=",", delimiter_expected_data=",", quotechar_actual_data='"', quotechar_expected_data='"', template_literals_dict=None):
        for file in (actual_file, expected_file):
            if not os.path.exists(file):
                raise Exception("Input file doesn't exists: ", file)
        #
        print("actual_file: ", actual_file)
        print("expected_file: ", expected_file)
        #
        with open(actual_file, mode='rt', encoding='utf-8') as actual_file, open(expected_file, mode='rt', encoding='utf-8') as expected_file:
            if len(delimiter_actual_data) == 1:
                actual_data = list(csv.reader(actual_file, delimiter=delimiter_actual_data, quotechar=quotechar_actual_data))
            else:
                actual_data = list(csv.reader((line.replace(delimiter_actual_data, chr(255)) for line in actual_file), delimiter=chr(255), quotechar=quotechar_actual_data))
            #
            if len(delimiter_expected_data) == 1:
                expected_data = list(csv.reader(expected_file, delimiter=delimiter_expected_data, quotechar=quotechar_expected_data))
            else:
                expected_data = list(csv.reader((line.replace(delimiter_expected_data, chr(255)) for line in expected_file), delimiter=chr(255), quotechar=quotechar_expected_data))
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_text_variable_with_text_file(self, actual_text, expected_file, template_literals_dict=None):
        if 'actual_data' not in locals():
            raise Exception("Input Actual data unknown.")
        #
        if not os.path.exists(expected_file):
            raise Exception("Input file doesn't exists: ", expected_file)
        #
        print("expected_file: ", expected_file)
        #
        actual_data = []
        for line in actual_text.split('\n'):
            actual_data.append(line.strip('\n').split(chr(255)))
        #
        with open(expected_file, mode='rt', encoding='utf-8') as expected_file:
            expected_data = []
            for line in expected_file.readlines():
                expected_data.append(line.strip('\n').split(chr(255)))
            #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_text_file_with_text_variable(self, actual_file, expected_text, template_literals_dict=None):
        if not os.path.exists(actual_file):
            raise Exception("Input file doesn't exists: ", actual_file)
        #
        if 'expected_text' not in locals():
            raise Exception("Input Expected data unknown.")
        #
        print("actual_file: ", actual_file)
        #
        with open(actual_file, mode='rt', encoding='utf-8') as actual_file:
            actual_data = []
            for line in actual_file.readlines():
                actual_data.append(line.strip('\n').split(chr(255)))
            #
        expected_data = []
        for line in expected_text.split('\n'):
            expected_data.append(line.strip('\n').split(chr(255)))
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_text_variables(self, actual_text, expected_text, template_literals_dict=None):
        if 'actual_data' not in locals():
            raise Exception("Input Actual data unknown.")
            #
        if 'expected_data' not in locals():
            raise Exception("Input Expected data unknown.")
            #
        actual_data = []
        for line in actual_text.split('\n'):
            actual_data.append(line.strip('\n').split(chr(255)))
        #
        expected_data = []
        for line in expected_text.split('\n'):
            expected_data.append(line.strip('\n').split(chr(255)))
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


    def compare_text_files(self, actual_file, expected_file, template_literals_dict=None):
        for file in (actual_file, expected_file):
            if not os.path.exists(file):
                raise Exception("Input file doesn't exists: ", file)
        #
        print("actual_file: ", actual_file)
        print("expected_file: ", expected_file)
        #
        with open(actual_file, mode='rt', encoding='utf-8') as actual_file, open(expected_file, mode='rt', encoding='utf-8') as expected_file:
            actual_data = []
            for line in actual_file.readlines():
                actual_data.append(line.strip('\n').split(chr(255)))
#            print(actual_data)
            #
            expected_data = []
            for line in expected_file.readlines():
                expected_data.append(line.strip('\n').split(chr(255)))
#            print(expected_data)
        #
        ArrayComparer.compare_data(self, actual_data, expected_data, template_literals_dict)


