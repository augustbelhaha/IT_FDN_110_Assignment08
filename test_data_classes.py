# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Test Data Classes
# # Description: The test file for data_classes.py
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/05/2023, Add Test Classes and Methods
# ABelhumeur, 12/09/2023, Edit test methods
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
import unittest
from data_classes import Person, Employee


# ---------- Setup Unit Test Classes ---------- #

class TestPerson(unittest.TestCase):

    def test_person_init(self):
        """
        Tests initializing a Person.
        """
        person = Person('August', 'Belhumeur')
        self.assertEqual('August', person.first_name)
        self.assertEqual('Belhumeur', person.last_name)
        print(person)

    def test_person_invalid_name(self):
        """
        Tests that a ValueError gets raised if there are number values in a name.
        """
        with self.assertRaises(ValueError):
            person = Person('123', 'Belhumeur')


    def test_person_str(self):
        """
        Tests that a Person is a string.
        """
        person = Person('August', 'Belhumeur')
        self.assertEqual('August Belhumeur', str(person))


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):
        """
        Tests initializing an Employee.
        """
        employee = Employee('August', 'Belhumeur', '2023-12-05', 5)
        self.assertEqual('August', employee.first_name)
        self.assertEqual('Belhumeur', employee.last_name)
        self.assertEqual('2023-12-05', employee.review_date)
        self.assertEqual(5, employee.review_rating)
        print(employee)

    def test_employee_invalid_review_date(self):
        """
        Tests that a value error is raised if the review_date is not the correct format.
        """
        with self.assertRaises(ValueError):
            employee = Employee('August', 'Belhumeur', '2023-12-5', 5)

    def test_employee_invalid_review_rating(self):
        """
        Tests that a value error is raised if the review rating is not an integer between 1 and 5.
        """
        with self.assertRaises(ValueError):
            employee = Employee('August', 'Belhumeur', '2023-12-05', 0)


if __name__ == '__main__':
    unittest.main()
