# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Presentation Classes
# # Description: Collection of all presentation classes to be used in Assignment08's program
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/09/2023, Edit to remove dependencies
# ------------------------------------------------------------------------------------------------- #

# Import Libraries

# Define Data Constants and Variables
menu_choice: str = ""  # Hold the choice made by the user


# ---------- Presentation Classes ---------- #

class IO:
    """
    A collection of presentation layer functions that manage user input and output.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays error messaging should an exception get called.
        :param message: Prints a string for custom error messaging or explaining how errors are addressed in
        the case of an exception.
        :param error: If there is an exception error, this parameter will print technical information.
        If there is no error, it will do nothing. By default, there is no error.
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def input_menu_choice(menu: str) -> str:
        """
        This function inputs the user's menu selection of either 1, 2, 3, or 4.
        :param menu: This variable is a string value that is the user's input.
        :return: Return the user's input.
        """
        global menu_choice
        menu_choice = input(menu)
        while menu_choice not in ['1', '2', '3', '4']:
            IO.output_error_messages(message="Please enter an option between 1 and 4")
            menu_choice = input(menu)
        return menu_choice

    @staticmethod
    def output_employee_data(employee_data: list, data_type: object) -> None:
        """
        Displays all entered employee review data, showing the names of the employees, the date of their review,
        and the rating that they received.
        :param employee_data: The list of all employee review data.
        :return: Returns nothing.
        """
        message: str = ""
        print("-" * 50)
        for employee in employee_data:
            if isinstance(employee, data_type):
                if employee.review_rating == 5:
                    message = " {} {} is rated as 5 (Leading)"
                elif employee.review_rating == 4:
                    message = " {} {} is rated as 4 (Strong)"
                elif employee.review_rating == 3:
                    message = " {} {} is rated as 3 (Solid)"
                elif employee.review_rating == 2:
                    message = " {} {} is rated as 2 (Building)"
                elif employee.review_rating == 1:
                    message = " {} {} is rated as 1 (Not Meeting Expectations)"
                print(message.format(employee.first_name, employee.last_name, employee.review_date,
                                     employee.review_rating))
        print("-" * 50)

    @staticmethod
    def input_employee_data(employee_data: list, data_type: object) -> list:
        """
        Asks the user to input information required for each employee, including the employee's first and last name,
        the date of their review, and the rating they received, which all gets appended to employee_data.
        :param employee_data: The list of all employee review data.
        :return: Returns the list of all employee review data.
        """
        try:
            employee = data_type()
            employee_first_name = str(input("Enter the employee's first name: "))
            employee_last_name = str(input("Enter the employee's last name: "))
            employee_review_date = input("Enter their review date in the format YYYY-MM-DD: ")
            review_rating_input = input("Enter their review rating from 1-5: ")
            employee_review_rating = int(review_rating_input)
            new_employee = data_type(first_name=employee_first_name, last_name=employee_last_name,
                                    review_date=employee_review_date, review_rating=employee_review_rating)
            employee_data.append(new_employee)
            print()
            print(f"{employee_first_name} {employee_last_name} was reviewed on {employee_review_date} \
and received the rating {employee_review_rating}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was an incorrect type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return employee_data


# Main Method: In case of running this file by mistake
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
