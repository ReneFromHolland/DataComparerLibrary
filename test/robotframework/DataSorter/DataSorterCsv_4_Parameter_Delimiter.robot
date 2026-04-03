*** Settings ***
Documentation     Feature: Sorting data${\n}
...     Sorting data from a file is based on Python cvs.reader and csv.writer.${\n}
...     Sorting is ascending and can be done on maximum 7 columns currently. Columns to be sorted has to be
...     added to a list which is presented to the module as an argument. Default will be sorted on the first column as string.${\n}
...     Sorting per column can be done as a string or as an integer.${\n}
...     In case the column number is added to the list of columns as a string, it will be sorted as a string.${\n}
...     In case the column number is added to the list of columns as an integer, it will be sorted as an integer.${\n}
...
...    Testcases in order to see if sorting of data works fine for different types of delimiters.

Library         DataComparerLibrary

Resource        ../module_variables.resource


*** Test Cases ***
Sorting data from a csv File - No parameters used - Default delimiter Comma
    [Documentation]  Sorting data from a csv File - No parameters used - Default delimiter Comma
    [Tags]  CSV  Delimiter  No_Parameters
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_comma.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_comma.csv


Sorting data from a csv File - Delimiter Comma
    [Documentation]  Sorting data from a csv File - Delimiter Comma
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_comma.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  delimiter=,
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_comma.csv


Sorting data from a csv File - Delimiter Pipe
    [Documentation]  Sorting data from a csv File - Delimiter Pipe
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_pipe.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_pipe.csv  delimiter=|
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_pipe.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_pipe.csv


Sorting data from a csv File - Delimiter Semicolon
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_semicolon.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_semicolon.csv  delimiter=;
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_semicolon.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_semicolon.csv


Sorting data from a csv File - Delimiter Tab
    [Documentation]  Sorting data from a csv File - Delimiter Tab
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_tab.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_tab.csv  delimiter='\t'
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_tab.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_tab.csv


Sorting data from a csv File - Delimiter @#@
    [Documentation]  Sorting data from a csv File - Delimiter @#@
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_@#@.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_@#@.csv  delimiter=@#@
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_@#@.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_@#@.csv


Sorting data from a csv File - Delimiter Comma different from delimiter @#@ used in file
    [Documentation]  Sorting data from a csv File - Delimiter Comma different from delimiter @#@ used in file
    [Tags]  CSV  Delimiter
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_@#@.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_@#@_parameter_comma.csv  delimiter=,
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_@#@_parameter_comma.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_@#@_parameter_comma.csv
