*** Settings ***
Library     DataComparerLibrary


*** Keywords ***
A File "${input_file_with_separate_lf}" has a separated LF
    Log  File "${input_file_with_separate_lf}" has been prepared.


Remove LF is performed on data in File "${input_file_with_separate_lf}" and the data is written to File "${output_file_without_separate_lf}"
    DataComparerLibrary.Remove Separate Lf  ${input_file_with_separate_lf}  ${output_file_without_separate_lf}


Replace Separated LF With "${replacement_string}" In The Data From File "${input_file_with_separate_lf}" is Performed And Written To File "${actual_output_file_lf_replaced_by_character_or_string}"
    #[Arguments]  ${input_file_with_separate_lf}  ${actual_output_file_lf_replaced_by_character_or_string}  ${replacement_string}
    DataComparerLibrary.Replace Separate Lf  ${input_file_with_separate_lf}  ${actual_output_file_lf_replaced_by_character_or_string}  ${replacement_string}


The Output File "${actual_output_file}" should be equal to the Expected File "${expected_output_file}"
    DataComparerLibrary.Compare Data Files  ${actual_output_file}  ${expected_output_file}
