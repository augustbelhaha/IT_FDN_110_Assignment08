# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 Processing Classes
# # Description: Collection of all processing classes to be used in Assignment08's program
# ChangeLog: (Who, When, What)
# ABelhumeur, 12/04/2023, Created Script
# ABelhumeur, 12/09/2023, Edited to remove dependencies
# ------------------------------------------------------------------------------------------------- #

# Import Libraries
import json

# Define Global Data Variables
file = None


# ---------- Processing Classes ---------- #

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, data_type: object):
        """
        This function reads JSON data from the specified file.
        :param file_name: A string indicating the specified file name.
        :param employee_data: The list of employee review data currently saved to the file.
        :return: Return the list of employee review data currently saved to the file.
        """
        dict_table: list[dict[str, str, str, int]] = []
        file = None
        try:
            file = open(file_name, "r")
            dict_table = json.load(file)
        except FileNotFoundError:
            file = open(file_name, 'w')
            json.dump(employee_data, file)
            raise FileNotFoundError("Text file not found. Creating file since it doesn't exist.")
        except Exception:
            raise Exception("Error: There was a problem reading the file.")
        finally:
            if not file.closed:
                file.close()
        employee_data: list[data_type] = []
        for row in dict_table:
            first_name = row.get('FirstName', '')
            last_name = row.get('LastName', '')
            review_date = row.get('ReviewDate', '')
            review_rating = row.get('ReviewRating', '')
            employee_data.append(data_type(first_name, last_name, review_date, review_rating))
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        This function saves all entered data to the JSON file without erasing existing entries.
        :param file_name: A string indicating the specified file name.
        :param employee_data: The list of all employee review data entered.
        :return: Returns the list of all employee review data.
        """
        try:
            file = open(file_name, "w")
            list_of_dictionary_data: list = []
            for employee in employee_data:
                employee_json: dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating,
                }
                list_of_dictionary_data.append(employee_json)
            json.dump(list_of_dictionary_data, file, indent=1)
            print("All review entries have been saved to the file 'EmployeeRatings.json'.")
            file.close()
        except TypeError:
            raise TypeError("Please check that the dats is a valid JSON format.")
        except Exception:
            raise Exception("There was a non-specific error.")
        finally:
            if not file.closed:
                file.close()
        return employee_data


# Main Method: In case of running this file by mistake
if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
