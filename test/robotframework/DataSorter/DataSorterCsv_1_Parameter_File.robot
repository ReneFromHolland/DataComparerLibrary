*** Settings ***
Documentation     Feature: Sorting data${\n}
...     Sorting data from a file is based on Python cvs.reader and csv.writer.${\n}
...     Sorting is ascending and can be done on maximum 7 columns currently. Columns to be sorted has to be
...     added to a list which is presented to the module as an argument. Default will be sorted on the first column as string.${\n}
...     Sorting per column can be done as a string or as an integer.${\n}
...     In case the column number is added to the list of columns as a string, it will be sorted as a string.${\n}
...     In case the column number is added to the list of columns as an integer, it will be sorted as an integer.${\n}
...
...    Testcases in order to check file handling in case of special situations.

Library         DataComparerLibrary

Resource        ../module_variables.resource


*** Test Cases ***
Sorting data from a csv File - Handling input File not present
    [Documentation]  Sorting data from a csv File - Handling input File not present
    [Tags]  Input_File  Missing_File
    Run Keyword And Expect Error  ('Error message: ', 'Exception', '–', Exception("Input file doesn't exists: ", '*input_file_not_present.csv'))  DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_not_present.csv  ${path_actual_output_files}${/}output_file_not_present.csv


Sorting data from a csv File - Empty file- No parameters used
    [Documentation]  Sorting data from a csv File - Empty file- No parameters used
    [Tags]  Input_File  Empty_File  No_Parameters  File_type
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_empty.csv  ${path_actual_output_files}${/}output_file_empty.csv
    DataComparerLibrary.Compare Data Files    ${path_actual_output_files}${/}output_file_empty.csv  ${path_expected_output_files}${/}output_file_empty.csv
