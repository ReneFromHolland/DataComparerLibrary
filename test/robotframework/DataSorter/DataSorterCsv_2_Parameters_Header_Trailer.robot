*** Settings ***
Documentation     Feature: Sorting data${\n}
...     Sorting data from a file is based on Python cvs.reader and csv.writer.${\n}
...     Sorting is ascending and can be done on maximum 7 columns currently. Columns to be sorted has to be
...     added to a list which is presented to the module as an argument. Default will be sorted on the first column as string.${\n}
...     Sorting per column can be done as a string or as an integer.${\n}
...     In case the column number is added to the list of columns as a string, it will be sorted as a string.${\n}
...     In case the column number is added to the list of columns as an integer, it will be sorted as an integer.${\n}
...
...    Testcases in order to see if optional header and trailer records are ignored for sorting.

Library         DataComparerLibrary

Resource        ../module_variables.resource


*** Test Cases ***
Sorting data from a csv File - Parameter number_of_header_lines and number_of_trailer_lines impliciet zero - Data present
    [Documentation]  Sorting data from a csv File - Parameter number_of_header_lines and number_of_trailer_lines impliciet zero - Data present
    [Tags]  CSV  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_comma.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_comma.csv


Sorting data from a csv File - Parameter number_of_header_lines and number_of_trailer_lines explicit zero - Data present
    [Documentation]  Sorting data from a csv File - Parameter number_of_header_lines and number_of_trailer_lines expliciet zero - Data present
    [Tags]  CSV  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines_delimiter_comma.csv  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  number_of_header_lines=0  number_of_trailer_lines=0
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_delimiter_comma.csv  ${path_expected_output_files}${/}output_file_data_lines_delimiter_comma.csv


Sorting data from a csv File - Header present
    [Documentation]  Sorting data from a csv File - Header present
    [Tags]  CSV  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_lines.txt  ${path_actual_output_files}${/}output_file_header_lines.txt  number_of_header_lines=2
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_lines.txt  ${path_expected_output_files}${/}output_file_header_lines.txt


Sorting data from a csv File - Trailer present
    [Documentation]  Sorting data from a csv File - Trailer present
    [Tags]  CSV  Sort_by_columns  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_trailer_lines.txt  ${path_actual_output_files}${/}output_file_trailer_lines.txt  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_trailer_lines.txt  ${path_expected_output_files}${/}output_file_trailer_lines.txt


Sorting data from a csv File - Header and Trailer present
    [Documentation]  Sorting data from a csv File - Header and Trailer present
    [Tags]  CSV  Sort_by_columns  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_trailer_lines.txt  number_of_header_lines=2  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_trailer_lines.txt  ${path_expected_output_files}${/}output_file_header_trailer_lines.txt


Sorting data from a csv File - Header and Data present
    [Documentation]  Sorting data from a csv File - Header and Data present
    [Tags]  CSV  Sort_by_columns  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_lines.txt  ${path_actual_output_files}${/}output_file_header_data_lines.txt  number_of_header_lines=2
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_lines.txt  ${path_expected_output_files}${/}output_file_header_data_lines.txt


Sorting data from a csv File - Data and Trailer present
    [Documentation]  Sorting data from a csv File - Data and Trailer present
    [Tags]  CSV  Sort_by_columns  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_data_trailer_lines.txt  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_trailer_lines.txt  ${path_expected_output_files}${/}output_file_data_trailer_lines.txt


Sorting data from a csv File - Header, Data and Trailer present
    [Documentation]  Sorting data from a csv File - Header, Data and Trailer present
    [Tags]  CSV  Sort_by_columns  Header  Data  Trailer
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines.txt  number_of_header_lines=2  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines.txt
