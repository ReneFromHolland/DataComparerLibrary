*** Settings ***
Resource        ../module_variables.resource
Resource        ../FileConverter/resources/FileConverterKeywords.resource


*** Test Cases ***
Scenario: Remove Separated LF from File "input_file_with_crlf_and_separate_lf.txt" and Write Result to File "actual_output_file_without_separate_lf"
    [Documentation]  Remove separated LF from file. Carriage return linefeed (CRLF) should remain.

    Given A File "${path_input_files}${/}input_file_with_crlf_and_separate_lf.txt" has a separated LF
    When Remove LF is performed on data in File "${path_input_files}${/}input_file_with_crlf_and_separate_lf.txt" and the data is written to File "${path_actual_output_files}${/}output_file_without_separate_lf.txt"
    Then The Output File "${path_actual_output_files}${/}output_file_without_separate_lf.txt" should be equal to the Expected File "${path_expected_output_files}${/}output_file_without_separate_lf.txt"
