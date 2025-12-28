*** Settings ***
Library         DataComparerLibrary


*** Test Cases ***
Remove CR and LF from string with CR and LF
    [Documentation]  Remove CR and LF from string
    VAR  ${input_string}  Line 1\rLine 2\r\nLine 3\n
    Log  ${input_string}
    ${output_string}  Remove Cr And Lf  ${input_string}
    Log  ${output_string}
    DataComparerLibrary.Compare Text Variables  ${output_string}  Line 1Line 2Line 3


Remove CR and LF from string without CR and LF
    [Documentation]  Remove CR and LF from string
    VAR  ${input_string}  This is a text string
    Log  ${input_string}
    ${output_string}  Remove Cr And Lf  ${input_string}
    Log  ${output_string}
    DataComparerLibrary.Compare Text Variables  ${output_string}  This is a text string
