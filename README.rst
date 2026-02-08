===================
DataComparerLibrary
===================

.. contents::
   :local:


Documentation
===================
See `keyword documentation`_ for available keywords and more information
about the library in general.

Preparation
===================

Installation
------------

If you already have Python with `pip <https://pip.pypa.io>`_ installed,
you can simply run:

.. sourcecode::

    pip install DataComparerLibrary
    pip install --upgrade DataComparerLibrary


Also the following pip package is needed:

.. sourcecode::

    pip install python-dateutil


Import statement for the DataComparerLibrary in Python
------------------------------------------------------

.. sourcecode::

  from DataComparerLibrary.datacomparer import DataComparer



DataComparer
============

Introduction
------------

The DataComparerLibrary can be used for:
    - comparing csv-files or text-files
    - comparing a 2d-matrix with a csv-file or text-file
    - comparing a csv-file or text-file with a 2d-matrix
    - comparing 2d-matrices

| The DataComparer will present the actual data and the expected data.
| In case a difference between actual and expected data is found an exception wil be given. Also these differences will be presented. 
| In Robot Framework the comparison result will be set to failed.
|

|

Special options
---------------

| A strait comparison can be made, but the DataComparerLibrary offers also some special comparison options described
  beneath.
|
| {PRESENT}:
| With {PRESENT} in the expected data file you can make clear that data of a field/cell of the actual data should be present.
  This can be helpful for fields that have constant changing values. For example generated id's.
|
| {EMPTY}:
| With {EMPTY} in the expected data file you can make clear that data of a field/cell of the actual data should be absent.
|
| {SKIP}:
| With {SKIP} in the expected data file you can make clear that the comparison of data of a field/cell or part of a field/cell
  of the actual data should be skipped. This can be helpful for fields or parts of fields that have constant changing
  values. For example time or generated id's.
|
| {INTEGER}:
| With {INTEGER} in the expected data file you can make clear that the data of a field/cell of the actual data should be an
  integer. This can be helpful for fields that have constant changing integer values. For example integer id's.
|
| {NOT(...)}:
| With {NOT(...)} in the expected data file you can make clear that data of a field/cell should not match the unexpected data.
| At "Examples comparing Actual Data with Expected Data" you can find some examples how to use it.
|
| {NOW()...:....}:
| With {NOW()} in the expected data file you can make clear that the data of a field/cell or part of a field/cell of the actual
  data should be (a part of) a date. You can let calculate the current or a date in the past or future. Calculation is
  based on the "relativedelta" method from Python. Also you can style the date in the format you want. This can be
  helpful for fields that have constant changing date values, but which date values have a fixed offset linked to the
  current date. At "Examples comparing Actual Data with Expected Data" you can find some examples how to use it.
|
| {DATETIME_FORMAT():YYYYMMDDHHMMSSFF6}:
| With {DATETIME_FORMAT():YYYYMMDDHHMMSSFF6} in the expected data file you can make clear that the data of a field/cell or part of a field/cell of the actual
  data should be (a part of) a date. At this moment it is processed as {SKIP}. In the future it will be changed into a check on date format, but
  not a specific date. For check on a specific expected date you can use {NOW()...:....}.
|
|
| Delimiter:
| Default delimiter is "," in case of an input file. You can use the option "delimiter_actual_data" and "delimiter_expected_data" to set another
  delimiter like ";" or "\t" for tab. It is also possible to use a multi-character delimiter like "@#@".
|
| Quotechar:
| Default quotechar is '"' in case of an input file. You can use the option "quotechar_actual_data" and/or "quotechar_expected_data" to set another
  quotechar.


Comparing Data
--------------


Examples of using the DataComparerLibrary for comparing data in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below there are some examples how to call the methods of the DataComparerLibrary in Python::


    a = DataComparer
    a.compare_data_files(self, actual_file, expected_file)
    a.compare_data_files(self, actual_file, expected_file, delimiter_actual_data=';', delimiter_expected_data=';')
    a.compare_data_files(self, actual_file, expected_file, delimiter_actual_data='@#@', delimiter_expected_data='@#@')
    a.compare_data_2d_array_with_file(self, actual_2d_matrix_data_input, expected_file, delimiter_expected_data='\t')
    a.compare_data_file_with_2d_array(self, actual_file, expected_2d_matrix_data_input, delimiter_actual_data=';')
    a.compare_data_2d_arrays(self, actual_2d_matrix_data_input, expected_2d_matrix_data_input)


Examples of using the DataComparerLibrary keywords for comparing data in Robot Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below there are some examples how to call the keywords of the DataComparerLibrary in Robot Framework:

.. sourcecode::

    *** Settings ***
    Library     DataComparerLibrary

    *** Test Cases ***
    Testcase_DataComparer
        Examples

    *** Keywords ***
    Examples
        Run Keyword And Continue On Failure  DataComparerLibrary.Compare Data Files  C:\\Users\\actual.csv   C:\\Users\\expected.csv
        DataComparerLibrary.Compare Data Files  C:\\Users\\actual.csv   C:\\Users\\expected.csv  delimiter_actual_data=;  delimiter_expected_data=;
        DataComparerLibrary.Compare Data Files  C:\\Users\\actual.csv   C:\\Users\\expected.csv  delimiter_actual_data=@#@  delimiter_expected_data=@#@
        DataComparerLibrary.Compare Data Files  C:\\Users\\actual.csv   C:\\Users\\expected.csv
        DataComparerLibrary.Compare Data 2d Array With File  ${actual_2d_matrix_data_input}  C:\\Users\\expected.csv  delimiter_expected_data=\t

        Set Variable  ${postcode}  52091
        ${expected_2d_matrix_data_input}=  Evaluate  [['NAME', 'STREET', 'NUMBER', 'CITY', 'POSTCODE'], ['JOHN', 'Lund gatan', 10, 'STOCKHOLM', '${postcode}']]

        DataComparerLibrary.Compare Data File With 2d Array  C:\\Users\\actual.csv  ${expected_2d_matrix_data_input}  delimiter_actual_data=;
        DataComparerLibrary.Compare Data 2d Arrays  ${actual_2d_matrix_data_input}  ${expected_2d_matrix_data_input}

        &{literal_dict}=  Create Dictionary  {lit_1}=${some_variable}
        ...                                  {lit_2}='Text with space'
        ...                                  {version}=${version}
        ...                                  {build_number}=${build_number}
        ...                                  {env}=${env}
        ...                                  {firstname}=${name}
        ...                                  {capital}='Stockholm'
        DataComparerLibrary.Compare Data Files  ${actual_input_file_template_literal}  ${expected_input_file_template_literal}  delimiter_actual_data=;  delimiter_expected_data=;  template_literals_dict=${literal_dict}

Examples comparing Actual Data with Expected Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below there is an example of actual and expected data with some different cases.



Based on current datetime = 2023-09-06 19:04:00  (example):


+--------------+---------------+--------------+---------------------------------+------------+-------------+
|                                   Actual csv file or 2d-array                                            |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| id           | name          | city         | start datetime                  | code       | password    |
+==============+===============+==============+=================================+============+=============+
| 87           | John          | London       | 2019-09-01 10:00:15             | abc1       | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| 88           | Bert          | Amsterdam    | 2023/09/06 19:02:00             |            | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| 89           | Klaas         | Brussel      | 23-8-6 12:04:17                 | 5ghi       | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| 90           | Joe           | Helsinki     | 08062025 12:04:17               | 99fg       | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| 91           | Mike          | Berlin       | 2023/09/06 19:02:00             | 123        | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| 92           | Kurt          | Paris        | 2023/09/06 19:02:00             | 123        | xxxxxxxx    |
+--------------+---------------+--------------+---------------------------------+------------+-------------+


+--------------+---------------+--------------+---------------------------------+------------+-------------+
|                                   Expected csv file or 2d-array                                          |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| id           | name          | city         | start datetime                  | code       | password    |
+==============+===============+==============+=================================+============+=============+
| {INTEGER}    | John          | London       | {NOW()-4Y5D:YYYY-MM-DD}         | abc1       | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| {INTEGER}    | Bert          | Amsterdam    | {NOW():YYYY/MM/DD} {SKIP}       | {EMPTY}    | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| {INTEGER}    | Klaas         | Brussel      | {NOW()-1M:YY-M-D} {SKIP}        | 5ghi       | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| {INTEGER}    | Joe           | Helsinki     | {NOW()+1Y9M2D:DDMMYYYY} {SKIP}  | {SKIP}     | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| {INTEGER}    | {NOT("Jack")} | Berlin       | {NOW():YYYY/MM/DD} {SKIP}       | {NOT(456)} | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+
| {INTEGER}    | {firstname}   | {capital}    | {NOW():YYYY/MM/DD} {SKIP}       | 123        | {PRESENT}   |
+--------------+---------------+--------------+---------------------------------+------------+-------------+


Comparing Text
--------------

Examples of using the DataComparerLibrary for comparing text in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below there are some examples how to call the methods of the DataComparerLibrary in Python:

.. sourcecode::

    a = DataComparer
    a.compare_text_files(self, actual_file, expected_file)
    a.compare_text_variable_with_text_file(self, actual_text_input, expected_file)
    a.compare_text_file_with_text_variable(self, actual_file, expected_text_input)
    a.compare_text_variables(self, actual_text_input, expected_text_input)


Examples of using the DataComparerLibrary keywords for comparing text in Robot Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below there are some examples how to call the keywords of the DataComparerLibrary in Robot Framework:

.. sourcecode::

    *** Settings ***
    Library     DataComparerLibrary

    *** Test Cases ***
    Testcase_DataComparer
        Examples

    *** Keywords ***
    Examples
        Run Keyword And Continue On Failure  DataComparerLibrary.Compare Text Files  C:\\Users\\actual.txt   C:\\Users\\expected.txt
        DataComparerLibrary.Compare Text Files  C:\\Users\\actual.txt   C:\\Users\\expected.txt
        DataComparerLibrary.Compare Text Files  C:\\Users\\actual.txt   C:\\Users\\expected.txt
        DataComparerLibrary.Compare Text Files  C:\\Users\\actual.txt   C:\\Users\\expected.txt
        DataComparerLibrary.Compare Text Variable With File  ${actual_text_input}  C:\\Users\\expected.txt
        DataComparerLibrary.Compare Text File With Text Variable  C:\\Users\\actual.txt  ${expected_text_input}
        DataComparerLibrary.Compare Text Variables  ${actual_text_input}  ${expected_text_input}



DataSorter
==========

Introduction
------------
The DataSorter can be used for sorting records in a csv file or text file.


Default sorting
---------------
The default sorting is alphabetically based in ascending order on column 0 on all records.


Special sorting
---------------

| With the DataSorter it is possible to tune the sorting of records.
|
| number_of_header_lines:
| Optional argument "number_of_header_lines" can be used to set the number of header records. These records will be excluded from sorting.
  In case this optional argument is not present the default value is set to 0.
|
| number_of_trailer_lines:
| Optional argument "number_of_trailer_lines" can be used to set the number of trailer records. These records will be excluded from sorting.
  In case this optional argument is not present the default value is set to 0.
|
| sort_on_columns_list:
| Optional argument "sort_on_columns_list" can be used to specify one or more columns on which should be sorted and in which order of columns.
  Sorting of a column can be done in an alphabetic or numeric way.
|
| delimiter:
| Optional argument "delimiter" can be used to set the delimiter.
  Default delimiter is "," in case of an input file. You can use the option "delimiter" to set another delimiter
  like ";" or "\t" for tab. It is also possible to use a multi-character delimiter like "@#@".


Examples of using the DataComparerLibrary keywords for sorting data in Robot Framework
----------------------------------------------------------------------------------------

Below there are some examples how to call the keywords of the DataComparerLibrary in Robot Framework:

.. sourcecode::

    *** Settings ***
    Library     DataComparerLibrary

    *** Test Cases ***
    Testcase_DataSorter
        Examples

    *** Keywords ***
    Examples
        # sorting examples
        #
        # Sorting alphabetic on column 0, 5 and 4
        ${sorting_column_0_5_4} =  create list   0  5  4
        # Sorting alphabetic on column 4 and 1 and numeric on colum 3
        ${sorting_column_4_3i_1} =  create list   4  ${3}  1


        Run Keyword And Continue On Failure  DataComparerLibrary.Sort Csv Files  C:\\Users\\unsorted.csv   C:\\Users\\sorted.csv
        DataComparerLibrary.Sort Csv Files  C:\\Users\\unsorted.csv   C:\\Users\\sorted.csv  number_of_header_lines=5  sort_on_columns_list=${sorting_column_0_5_4}  number_of_trailer_lines=5  delimiter=;
        DataComparerLibrary.Sort Csv Files  C:\\Users\\unsorted.csv   C:\\Users\\sorted.csv  number_of_header_lines=4  sort_on_columns_list=${sorting_column_4_3i_1}  delimiter=@#@
        DataComparerLibrary.Sort Csv Files  C:\\Users\\unsorted.csv   C:\\Users\\sorted.csv  number_of_trailer_lines=2  delimiter=\t
        DataComparerLibrary.Sort Csv Files  C:\\Users\\unsorted.csv   C:\\Users\\sorted.csv


FileConverter
=============

Introduction
------------

Records in files can be ended by carriage return line feed (CRLF). In some situations separate line feeds (LF) are
present within records. For example for an easy way of sorting records this can be a problem.

DataComparerLibrary keywords for preparing data in Robot Framework
------------------------------------------------------------------

The keywords "Remove Separate Lf" and "Replace Separate Lf" support removing/replacing a separate Lf in the data from
the input file. The result will be written to an output file.


Examples of using the DataComparerLibrary keywords for preparing data in Robot Framework
----------------------------------------------------------------------------------------

Below there are some examples how to call the keywords of the DataComparerLibrary in Robot Framework:

.. sourcecode::

    *** Settings ***
    Library     DataComparerLibrary

    *** Test Cases ***
    Testcase_FileConverter
        Remove Separate LF From Data In File
        Replace Separated LF With Character Or String From Data In File

    *** Keywords ***
    Remove Separate LF From Data In File
        DataComparerLibrary.Remove Separate Lf  ${path_actual_input_files}\\input_file_with_lf.txt  ${path_actual_output_files}\\output_file_without_lf.txt


    Replace Separated LF With Character Or String From Data In File
        DataComparerLibrary.Replace Separate Lf  ${input_file_with_separate_lf}   ${output_file_lf_replaced_by_character_or_string}   ${replacement_string}
        DataComparerLibrary.Replace Separate Lf  input_file_with_separate_lf.txt  output_file_lf_replaced_by_character_or_string.txt  abc
        DataComparerLibrary.Replace Separate Lf  input_file_with_separate_lf.txt  output_file_lf_replaced_by_character_or_string.txt  x
        DataComparerLibrary.Replace Separate Lf  input_file_with_separate_lf.txt  output_file_lf_replaced_by_character_or_string.txt  ${SPACE}




.. _Keyword Documentation: https://https://github.com/ReneFromHolland/DataComparerLibrary/blob/main/DataComparerLibraryKeywords.html
