# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Data Classes
# # Description: Collection of all data classes to be used in Assignment08's program
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
from datetime import date


# ---------- Inherited Data Classes ---------- #

class Person:
    """
    A Super / Parent class for storing data belonging to multiple persons, including first and last name.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Define variables for the class "Person".
        :param first_name: The person's first name.
        :param last_name: The person's last name.
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Gets first_name as an instanced variable.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Returns an error if first_name is set as anything but alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("First name can only contain alphabetic characters.")

    @property
    def last_name(self):
        """
        Gets last_name as an instanced variable.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Returns an error if last_name is set as anything but alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("Last name can only contain alphabetic characters.")

    def __str__(self):
        """
        :return: A string to return the instance of a Person's first and last name.
        """
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    """
    A subclass of Person, Employee stores data regarding the date that the employee's review took place and the rating
    assigned in the review, in addition to storing the Employee's first and last name inherited from Person.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01",
                 review_rating: int = 3):
        """
        Define variables for the subclass, Employee, and call existing variables from the super class, Person.
        :param first_name: The employee's first name, inherited from Person.
        :param last_name: The employee's last name, inherited from Person.
        :param review_date: The date the employee's review occurred. Defaults to 1900-01-01.
        :param review_rating: The reviewing rating of the employee's performance on a scale of 1-5. Has a default
        value of 3.
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Gets review_date as an instanced variable.
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Sets the value input for an entered review_date instance as a string, so that the entered value matches
        correct date formatting YYYY-MM-DD.
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Gets review_rating as an instanced variable.
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """
        Sets the value input for a review_rating instance as an integer between 1 and 5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please only enter a value between 1 and 5.")

    def __str__(self):
        """
        :return: A string to return the instance of Student, including inherited variables.
        """
        return f"{self.first_name} {self.last_name}, {self.review_date}, received the rating {self.review_rating}."


# Main Method: In case of running this file by mistake
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
