# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Test Processing Classes
# # Description: The test file for processing_classes.py
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/06/2023, Add testing for read / write to file
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
import json
import unittest
import tempfile
from processing_classes import FileProcessor
from data_classes import Employee


# Setup Unit Tests

class TestFileProcessor(unittest.TestCase):

    def setUp(self):  # Set up temp file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):  # Close temp file after testing
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        sample_data = [{'FirstName': 'Grace', 'LastName': 'Cooper', 'ReviewDate': '2022-01-01', 'ReviewRating': 4}]

        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, sample_data)

        self.assertEqual(sample_data[0]['FirstName'], employees[0].first_name)
        self.assertEqual(sample_data[0]['LastName'], employees[0].last_name)
        self.assertEqual(sample_data[0]['ReviewDate'], employees[0].review_date)
        self.assertEqual(sample_data[0]['ReviewRating'], employees[0].review_rating)

    def test_write_employee_data_to_file(self):
        sample_data = [
            Employee('August', 'Belhumeur', '2023-12-06', 5)
        ]
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)

        with open(self.temp_file_name, 'r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        self.assertEqual(sample_data[0].first_name, file_data[0]['FirstName'])
        self.assertEqual(sample_data[0].last_name, file_data[0]['LastName'])
        self.assertEqual(sample_data[0].review_date, file_data[0]['ReviewDate'])
        self.assertEqual(sample_data[0].review_rating, file_data[0]['ReviewRating'])


if __name__ == '__main__':
    unittest.main()
