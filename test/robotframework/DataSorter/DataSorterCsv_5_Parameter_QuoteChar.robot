*** Settings ***
Documentation     Feature: Sorting data${\n}
...     Sorting data from a file is based on Python cvs.reader and csv.writer.${\n}
...     Sorting is ascending and can be done on maximum 7 columns currently. Columns to be sorted has to be
...     added to a list which is presented to the module as an argument. Default will be sorted on the first column as string.${\n}
...     Sorting per column can be done as a string or as an integer.${\n}
...     In case the column number is added to the list of columns as a string, it will be sorted as a string.${\n}
...     In case the column number is added to the list of columns as an integer, it will be sorted as an integer.${\n}
...
...    Testcases in order to see if sorting of data works fine for different types of quote chararcters.

Library         DataComparerLibrary

Resource        ../module_variables.resource


*** Test Cases ***

#+++++++++++++++++ create  files
#Quotechar

#    number_of_header_lines=0, number_of_trailer_lines=0, sort_on_columns_list=None, delimiter=',', quotechar=None):


No Quotechar - default
Single
Double
Mix