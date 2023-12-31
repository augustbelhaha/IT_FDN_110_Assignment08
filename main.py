# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Main
# # Description: The main program to run for Assignment08 to demonstrate lessons from the course.
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/09/2023, Edited to include code that helps remove dependencies from modules.
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
from presentation_classes import IO
from processing_classes import FileProcessor
from data_classes import Employee

# Define the Data Constants
MENU: str = '''
---- Employee Ratings ----
  Select from the following menu:  
    1. Enter new employee rating data.
    2. Show current employee rating data.
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "EmployeeRatings.json"

# Define the Data Variables
employees: list = []  # A table of employee data
menu_choice: str = ""  # Hold the choice made by the user


################################################################
# ---------- Main Program: Present and Process Data ---------- #

# When the program starts, read the file data into a list of lists (table) and extract data from the file
try:
    employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees, data_type=Employee)
    for employee in employees:
        print(employee)

except FileNotFoundError as e:
    IO.output_error_messages(e)

except Exception as e:
    IO.output_error_messages(e)


# Present and Process Data
while True:

    # Present the menu of choices
    menu_choice = IO.input_menu_choice(MENU)

    # Enter new employee rating data
    if menu_choice == "1":
        students = IO.input_employee_data(employee_data=employees, data_type=Employee)
        continue

    # Show current employee rating data
    elif menu_choice == "2":
        IO.output_employee_data(employee_data=employees, data_type=Employee)
        continue

    # Save data to a file
    elif menu_choice == "3":
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        except TypeError as e:
            IO.output_error_messages(e)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    # Exit the Program (Stop the loop)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
