"""
To get details of employees who's salary is > 9000.
"""

from my_utils.csv_operations import HandleCSV
from my_utils.pretty_printer import task_one_format


def do_task_one():
    print("Employees who's salary is >9000")
    for emp in HandleCSV.read_csv_line_by_line():
        if int(emp["SALARY"]) > 9000:
            # if salary is >9000, print dictionary with only name, email and phone number
            print(task_one_format(emp))
