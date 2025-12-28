*** Settings ***
Resource        ../FileConverter/resources/FileConverterKeywords.resource
Resource        ../module_variables.resource


*** Test Cases ***
Scenario Outline: Replace Separated LF With Character Or String in File
    [Template]  Scenario Outline: Replace Separated LF With Character Or String In File
    # Examples
    # replacement_string    input_file_with_separate_lf                                      actual_output_file_lf_replaced_by_character_or_string                 expected_output_file_lf_replaced_by_character_or_string
    €                       ${path_input_files}${/}input_file_with_crlf_and_separate_lf.txt  ${path_actual_output_files}${/}output_file_lf_replaced_by_€.txt       ${path_expected_output_files}${/}output_file_lf_replaced_by_€.txt
    ${SPACE}                ${path_input_files}${/}input_file_with_crlf_and_separate_lf.txt  ${path_actual_output_files}${/}output_file_lf_replaced_by_space.txt   ${path_expected_output_files}${/}output_file_lf_replaced_by_space.txt
    aBc                     ${path_input_files}${/}input_file_with_crlf_and_separate_lf.txt  ${path_actual_output_files}${/}output_file_lf_replaced_by_aBc.txt     ${path_expected_output_files}${/}output_file_lf_replaced_by_aBc.txt


*** Keywords ***
Scenario Outline: Replace Separated LF With Character Or String In File
    [Arguments]  ${replacement_string}  ${input_file_with_separate_lf}  ${actual_output_file_lf_replaced_by_character_or_string}  ${expected_output_file_lf_replaced_by_character_or_string}
    #
    Given A File "${input_file_with_separate_lf}" Has A Separated LF
    When Replace Separated LF With "${replacement_string}" In The Data From File "${input_file_with_separate_lf}" is Performed And Written To File "${actual_output_file_lf_replaced_by_character_or_string}"
    Then The Output File "${actual_output_file_lf_replaced_by_character_or_string}" should be equal to the Expected File "${expected_output_file_lf_replaced_by_character_or_string}"
