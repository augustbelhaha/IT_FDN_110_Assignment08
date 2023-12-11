# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Test Presentation Classes
# # Description: The test file for presentation_classes.py
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/06/2023, Add test class and methods
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee


# ---------- Setup Unit Test Classes ---------- #

class TestIO(unittest.TestCase):

    def test_input_menu_choice(self):
        """
        Test selecting a menu option.
        """
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice("test")
            self.assertEqual('2', choice)

    def test_input_employee_data(self):
        """
        Test inputting employee data.
        """
        with patch('builtins.input', side_effect=['August', 'Belhumeur', '2023-12-06', 5]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, data_type=Employee)
            self.assertEqual('August', employees[0].first_name)
            self.assertEqual('Belhumeur', employees[0].last_name)
            self.assertEqual('2023-12-06', employees[0].review_date)
            self.assertEqual(5, employees[0].review_rating)

    def test_input_employee_data_incorrect_data(self):
        """
        Test that inputted employee data values correctly call ValueErrors.
        """
        with patch('builtins.input', side_effect=['August', 'Belhumeur', '2023-12-06', 99]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, data_type=Employee)
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
