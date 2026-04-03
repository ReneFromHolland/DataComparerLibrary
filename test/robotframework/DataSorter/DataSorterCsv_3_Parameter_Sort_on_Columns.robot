*** Settings ***
Documentation     Feature: Sorting data${\n}
...     Sorting data from a file is based on Python cvs.reader and csv.writer.${\n}
...     Sorting is ascending and can be done on maximum 7 columns currently. Columns to be sorted has to be
...     added to a list which is presented to the module as an argument. Default will be sorted on the first column as string.${\n}
...     Sorting per column can be done as a string or as an integer.${\n}
...     In case the column number is added to the list of columns as a string, it will be sorted as a string.${\n}
...     In case the column number is added to the list of columns as an integer, it will be sorted as an integer.${\n}
...
...    Testcases in order to see if sorting of data works fine.

Library         DataComparerLibrary

Resource        ../module_variables.resource


*** Test Cases ***
Sorting data from a csv File - Data present - Sort on column 1 as integer and column 0 alphabetically
    [Documentation]  Sorting data from a csv File - Data present - Sort on column 1 as integer and column 0 alphabetically
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_1i_0} =  ${1}  0
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_data_lines.txt  ${path_actual_output_files}${/}output_file_data_lines_sort_1i_0.txt  sort_on_columns_list=${sorting_column_1i_0}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_data_lines_sort_1i_0.txt  ${path_expected_output_files}${/}output_file_data_lines_sort_1i_0.txt


Sorting data from a csv File - Header, Data and Trailer present - Default sort on column 0 alphabetically - No sorting list
    [Documentation]  Sorting data from a csv File - Default sort on column 0 alphabetically - No sorting list
    [Tags]  CSV  Sort_by_columns
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  number_of_header_lines=2  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt


Sorting data from a csv File - Header, Data and Trailer present - Default sort on column 0 alphabetically - Sorting list empty
    [Documentation]  Sorting data from a csv File - Default sort on column 0 alphabetically - Sorting list empty
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_absent} =  @{EMPTY}
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_absent}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt


Sorting data from a csv File - Header, Data and Trailer present - Sort on column 0 alphabetically
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon - Header, Data and Trailer present - Sort on column 0 alphabetically
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_0} =  0
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_0}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_0.txt


Sorting data from a csv File - Header, Data and Trailer present - Sort on column 1 alphabetically
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon - Header, Data and Trailer present - Sort on column 1 alphabetically
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_1} =  1
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_1}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_1.txt


Sorting data from a csv File - Header, Data and Trailer present - Sort on column 1 as integer
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon - Header, Data and Trailer present - Sort on column 1 as integer
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_1i} =  ${1}
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1i.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_1i}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1i.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_1i.txt


Sorting data from a csv File - Header, Data and Trailer present - Sort on column 1 as integer and column 0 alphabetically
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon - Header, Data and Trailer present - Sort on column 1 as integer and column 0 alphabetically
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_1i_0} =  ${1}  0
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1i_0.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_1i_0}
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines_sort_1i_0.txt  ${path_expected_output_files}${/}output_file_header_data_trailer_lines_sort_1i_0.txt


Sorting data from a csv File - Header, Data and Trailer present - Sort on out of range column 4 alphabetically
    [Documentation]  Sorting data from a csv File - Delimiter Semicolon - Header, Data and Trailer present - Sort on out of range column 4 alphabetically
    [Tags]  CSV  Sort_by_columns
    VAR  @{sorting_column_4} =  4
    ${msg} =  Run Keyword And Expect Error  ("Probably selected column doesn't exist. Correct argument 'sort_on_columns_list'. Error message: ", 'IndexError', '–', IndexError('list index out of range'))  DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.txt  ${path_actual_output_files}${/}output_header_data_trailer_lines_sort_index_put_of_range.txt  number_of_header_lines=2  number_of_trailer_lines=3  sort_on_columns_list=${sorting_column_4}
    Log  ${msg}


Sorting data from a csv File - Header, Data and Trailer present - file type csv
    [Documentation]  Sorting data from a csv File - Header, Data and Trailer present - file type csv
    [Tags]  CSV  Header  Data  Trailer  File_type
    DataComparerLibrary.Sort CSV File  ${path_input_files}${/}input_file_header_data_trailer_lines.csv  ${path_actual_output_files}${/}output_file_header_data_trailer_lines.csv  number_of_header_lines=2  number_of_trailer_lines=3
    DataComparerLibrary.Compare Data Files  ${path_actual_output_files}${/}output_file_header_data_trailer_lines.csv  ${path_expected_output_files}${/}output_file_header_data_trailer_lines.csv
