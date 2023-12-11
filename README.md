# <span style="color: orange;">Assignment 08 Application Documentation</span>
This file provides documentation for all code in Assignment08.

August Belhumeur\
12/09/2023\
IT FDN 110\
Assignment 08 Documentation\
[Github Link](https://github.com/augustbelhaha/IT_FDN_110_Assignment08)

****
## <span style="color: orange;">Main (main.py)</span>
### Description
This is the main program for Assignment08, designed to demonstrate lessons from the course and Module08.
The program manages employee rating data through a menu-driven interface. It utilizes the modules presentation_classes,
processing_classes, and data_classes to separate concerns and enhance code modularity and re-usability.

### Import Required Libraries

```py
# Import Libraries
from presentation_classes import IO
from processing_classes import FileProcessor
from data_classes import Employee
```
- From presentation_classes.py module, import the class "IO", which stands for "input / output"
- From processing_classes.py module, import the class "FileProcessor"
- From data_classes.py module, import the class "Employee", which is inherited from the class "Person"

### Data Constants
- **MENU:** A menu displayed to input the user's choices
```angular2html
---- Employee Ratings ----
  Select from the following menu:  
    1. Enter new employee rating data.
    2. Show current employee rating data.
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
```
- **FILE_NAME:** The name of the file used to store employee's ratings **(EmployeeRatings.json)**

### Data Variables
- **employees:** A list (or table) of employee data.
- **menu_choice:** A string that holds the user's menu choice

### Main Program: Presenting and Processing Data

1. Read Data from File

```py
# When the program starts, read the file data into a list of lists (table) and extract data from the file
try:
    employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees, data_type=Employee)
    for employee in employees:
        print(employee)

except FileNotFoundError as e:
    IO.output_error_messages(e)

except Exception as e:
    IO.output_error_messages(e)
```
- Attempts to read data from the file specified in FILE_NAME using the module processing_classes.py and the class FileProcessor.
- It prints the employee data from the file to the user automatically when the program is run.
- The employee data retrieved from the file is appended to the data class Employee.
- Errors:
  - If the specified file cannot be found, it will print error messaging and create the file.
  - If any other exception is thrown, it will print error messaging.


2. Menu Driven Loop
```py
# Present and Process Data
while True:

    # Present the menu of choices
    menu_choice = IO.input_menu_choice(MENU)
```
- Continuously presents the menu of choices to the user.
- Executes corresponding actions based on the user's choice.

```py
# Enter new employee rating data
    if menu_choice == "1":
        students = IO.input_employee_data(employee_data=employees, data_type=Employee)
        continue
```
- If the user chooses menu option 1, run the method "input_employee_data" from the class "IO" to allow the user to enter
new employee review rating data.
- Then, present the menu of choices to the user again.

```py
# Show current employee rating data
    elif menu_choice == "2":
        IO.output_employee_data(employee_data=employees, data_type=Employee)
        continue
```
- If the user chooses menu option 2, run the method "output_employee_data" from the class "IO" to display all current
employee review rating data back to the user.
- Then, present the menu of choices to the user again.

```py
# Save data to a file
    elif menu_choice == "3":
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        except TypeError as e:
            IO.output_error_messages(e)
        except Exception as e:
            IO.output_error_messages(e)
        continue
```
- If the user chooses menu option 3, run the method "write_employee_data_to_file" from the class "FileProcessor" to save 
all entered employee review rating data to the .json file specified under FILE_NAME.
- Error handling displays error messaging in case the data trying to be entered to the file is of the wrong type or format.
It also displays error messaging for any other unknown Exception.
- Then, present the menu of choices to the user again.

```py
# Exit the Program (Stop the loop)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")
```
- If the user chooses menu option 4, the continuous loop ends.
- If the user enters an option in the menu that is anything other than 1, 2, 3, or 4, then it presents the menu options
again and tells the user that these numbers are the only valid options.

3. Program Termination
```py
print("Program Ended")
```
- Displays "Program Ended" when the user chooses to exit the program.


****
## <span style="color: orange;">Data Classes (data.classes.py)</span>
### Description
This module contains the data classes designed for use in Assignment08's main program. The classes
include a super/parent class called Person and a subclass called Employee. The Person class stores
information about individual people, including a first and last name, and the Employee class stores information
specific to employees, including the date of a review and the rating received in the review.

### Import Required Libraries
```py
# Import Libraries
from datetime import date
```
- From the Python module datetime, import the class "date"

### Classes
#### Person
A super/parent class for storing data belonging to multiple persons, including first and last names.

*Methods:*

1. `def __init__(self, first_name: str = "", last_name: str = ""):`
   1. Initializes a Person and defines the variables, which must include a first and last name.
2. `def first_name(self):`
   1. Gets input for a person's first name as an instanced variable.
3. `def first_name(self, value: str):`
   1. A setter for the variable "first_name" that includes error handling to ensure that a first name is a string and contains only alphabetic characters.
4. `def last_name(self):`
   1. Gets input for a person's last name as an instanced variable.
5. `def last_name(self, value: str):`
   1. A setter for the variable "last_name" that includes error handling to ensure that a last name is a string and contains only alphabetic characters.
6. `def __str__(self):`
   1. Provides a human-readable representation of the class instance. A method to return a string of an instanced person in the correct syntax to display a first name and then the last name with a space in between, like "Jane Doe".

#### Employee
A subclass of Person, Employee stores data regarding the date that the employee's review took place and the rating 
assigned in the review, in addition to storing the employee's first and last names inherited from Person.

*Methods:*

1. `def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):`
   1. Initializes and defines variables for the subclass, Employee. It calls existing variables from the super class, Person, including first and last name, and requires additional parameters for the date of the employee's review and the rating received.
2. `def review_date(self):`
   1. Gets input for the date of the employee's review as an instanced variable.
3. `def review_date(self, value: str):`
   1. A setter for the variable "review_date" that provides error handling if the date is entered in the wrong format. The date should follow the format YYYY-MM-DD.
4. `def review_rating(self):`
   1. Gets input for the rating received from the review as an instanced variable.
5. `def review_rating(self, value: int):`
   1. A setter for the variable "review_rating" that provides error handling to ensure that the rating entered is a number between 1 and 5.
6. `def __str__(self):`
   1. Provides a human-readable representation of the class instance. A method to return a string of an instanced employee in the correct syntax. The returned string should read like "Jane Doe, 1900-01-01, received the rating 3."

#### Main Method
```py
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
```
The script includes a main method to remind users that the file is not meant to be run directly. 
The classes are intended to be imported and used in other programs or applications.

#### Usage
To use these classes, import them into your main program. For example:
```py
from data_classes import Person, Employee

# Create instances of the classes
person_instance = Person(first_name="John", last_name="Doe")
employee_instance = Employee(first_name="Jane", last_name="Doe", review_date="2023-12-09", review_rating=4)

# Print string representations
print(person_instance)       # Output: John Doe
print(employee_instance)     # Output: Jane Doe, 2023-12-09, received the rating 4.
```
    

****
## <span style="color: orange;">Processing Classes (processing_classes.py)</span>
### Description
This module is a collection of file processing methods designed to work with JSON formatting. It includes methods for 
reading employee data from a file and writing employee data to a file. These functions are intended to handle the 
interaction between the program and a JSON file containing employee review data.

### Import Required Libraries
```py
# Import Libraries
import json
```
- From the Python module datetime, import json

### Define Data Variables
- **file = None** Set file to None as a global variable to be used in classes in this module.

### Classes
#### FileProcessor
A collection of processing layer functions that work with Json files.

*Methods:*
1. `def read_employee_data_from_file(file_name: str, employee_data: list, data_type: object):`
   1. This method reads JSON data from the specified file and returns the list of employee review data currently saved to the file.
   2. Parameters:
      1. `file_name: str` A string indicating the specified file name. 
      2. `employee_data: list` The list of employee review data currently saved to the file. 
      3. `data_type: object` The type of data class (e.g., Employee) used to represent individual entries.
   3. Returns:
      1. `employee_data: list` Returns the list of employee review data currently saved to the file.
2. `def write_employee_data_to_file(file_name: str, employee_data: list):`
   1. This method saves all entered data to the JSON file without erasing existing entries and returns the list of all employee review data.
   2. Parameters:
      1. `file_name: str` A string indicating the specified file name.
      2. `employee_data: list` The list of all employee review data entered.
   3. Returns:
      1. `employee_data: list` Returns the list of all employee review data.

#### Main Method
```py
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
```
The script includes a main method to remind users that the file is not meant to be run directly. 
The classes are intended to be imported and used in other programs or applications.

#### Usage
To use these classes, import them into your main program. For example:
```py
from processing_classes import FileProcessor
```


****
## <span style="color: orange;">Presentation Classes (presentation_classes.py)</span>
### Description
This module is a collection of presentation layer methods designed to manage user input and output in 
Assignment08's program. These functions handle the display of error messages, user input for menu choices, 
and the presentation of employee review data.

### Classes
#### IO
A collection of presentation layer functions that manage user input and output.

*Methods:*
1. `def output_error_messages(message: str, error: Exception = None):`
   1. This function displays error messaging should an exception get called.
   2. Parameters:
      1. `message: str` Prints a string for custom error messaging or explaining how errors are addressed in the case of an exception.
      2. `error: Exception = None` If there is an exception error, this parameter will print technical information. If there is no error, it will do nothing. By default, there is no error.
   3. Returns:
      1. Returns nothing
2. `def input_menu_choice(menu: str) -> str:`
   1. This method inputs the user's menu selection of either 1, 2, 3, or 4.
   2. Parameters:
      1. `menu: str` A string value representing the user's input.
   3. Returns:
      4. `str:` The user's input
3. `def output_employee_data(employee_data: list, data_type: object) -> None:`
   1. This method displays all entered employee review data back to the user, showing the names of the employees, the date of their review, and the rating that they received.
   2. Parameters:
      1. `employee_data: list` The list of all employee review data.
      2. `data_type: object` The type of data class (e.g., Employee) used to represent individual entries.
   3. Returns:
      1. Returns Nothing
4. `def input_employee_data(employee_data: list, data_type: object) -> list:`
   1. This method asks the user to input information required for each employee, including the employee's first and last name, the date of their review, and the rating they received, which all gets appended to `employee_data: list`.
   2. Parameters:
      1. `employee_data: list` The list of all employee review data.
      2. `data_type: object` The type of data class (e.g., Employee) used to represent individual entries.
   3. Returns:
      1. `list:` The list of all employee review data.


#### Main Method
```py
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
```
The script includes a main method to remind users that the file is not meant to be run directly. 
The classes are intended to be imported and used in other programs or scripts.

#### Usage
To use these classes, import them into your main program. For example:
```py
from presentation_classes import IO
```