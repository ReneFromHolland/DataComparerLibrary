*** Settings ***
Library            OperatingSystem

Resource            ../module_variables.resource

Variables           resources/module_variables.yaml

Suite Setup         Module Suite Setup


*** Keywords ***
Module Suite Setup
    Log  ${module_name}
    Initialize Module Variables  ${module_name}
    Remove Files  ${path_actual_output_files}${/}*.txt