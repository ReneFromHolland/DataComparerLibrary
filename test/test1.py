from DataComparerLibrary import DataComparer

# Input files
actual_file   = "C:\\Users\\USER\\Documents\\Tool projecten\\Robot Framework Verzamelmap\\RobotDemo-master-Probeersel\\data_vergelijker\\actueel_resultaat\\actual.csv"
expected_file = "C:\\Users\\USER\\Documents\\Tool projecten\\Robot Framework Verzamelmap\\RobotDemo-master-Probeersel\\data_vergelijker\\verwacht_resultaat\\expected_equal.csv"


a = DataComparer()
a.compare_data_files(actual_file, expected_file, delimiter_actual_data=';', delimiter_expected_data=';')
a.compare_data_files(actual_file, expected_file, delimiter_actual_data=';', delimiter_expected_data=';', quotechar_actual_data=None, quotechar_expected_data=None)
a.compare_data_files(actual_file, expected_file)
actual_data_input = [['3', '1.1', '4', '7', '2023-05-27 12:00'],
                     ['1', '0', '2', '9', '2023-05-29 12:00'],
                     ['', '2', '0', '1', '5'],
                     ['5.1', '8', '1', '0', '3'],
                     ['3', '', '2023-06-19', '3', '2023-06-08']]

a.compare_data_files(actual_data_input, expected_file)

a.compare_data_files(actual_file, expected_file)

