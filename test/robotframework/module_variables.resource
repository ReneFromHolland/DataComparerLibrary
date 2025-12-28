*** Settings ***
Variables           general_variables.yaml


*** Variables ***
${path_input_files}
${path_actual_output_files}
${path_expected_output_files}


*** Keywords ***
Initialize Module Variables
    [Arguments]  ${module_name}
    VAR  ${path_input_files}            ${EXECDIR}${/}${relative_testdata_path}${/}${module_name}${/}${inputfolder}  scope=GLOBAL
    VAR  ${path_actual_output_files}    ${EXECDIR}${/}${relative_testdata_path}${/}${module_name}${/}${actual_output_folder}  scope=GLOBAL
    VAR  ${path_expected_output_files}  ${EXECDIR}${/}${relative_testdata_path}${/}${module_name}${/}${expected_output_folder}  scope=GLOBAL
