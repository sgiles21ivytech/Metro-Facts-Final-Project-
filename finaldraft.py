""" In this final draft this program will display introduction page with two buttons
for either Employee or Supervisor, once they make the selection.
This will be controlled with classes and SQL Database"""

from tkinter import *
from tkinter import ttk  # Import ttk for dropdown menus
import sqlite3


# Parent Class for Staff Access (unchanged)
class StaffAccess:
    def __init__(self, name, access_id, role):
        self.name = name
        self.access_id = access_id
        self.role = role


# Subclass for Employee (unchanged)
class Employee(StaffAccess):
    def __init__(self, name, access_id, role, desk_number, sales_id):
        super().__init__(name, access_id, role)
        self.desk_number = desk_number
        self.sales_id = sales_id


# Subclass for Supervisor (unchanged)
class Supervisor(StaffAccess):
    def __init__(self, name, access_id, role, office_number, clearance_code):
        super().__init__(name, access_id, role)
        self.office_number = office_number
        self.clearance_code = clearance_code


# Create employee instances (unchanged)
employees = [
    Employee("Jerry Clark", 1234, "Employee", 10, "EMP-001"),
    Employee("Sarah Gordon", 5678, "Employee", 15, "EMP-002"),
    Employee("Victor Plain", 9012, "Employee", 20, "EMP-003"),
]


# Function to populate statistics with example data
def populate_stats():
    return


# Function to display statistics based on selection (unchanged)
def display_stats(view, period):
    return


def intro_window():
    return


def employee_window():
    employee_root = Tk()
    employee_root.title("Metro Facts - Employee View")

    # Dropdown menus for period (unchanged)

    # Statistics labels
    title_label = Label(employee_root, text="Stats", font=("Roboto", 12, "bold"))
    title_label.pack(pady=10)
    value_label = Label(employee_root, text="Total", font=("Roboto", 12, "bold"))
    value_label.pack()

    # Labels for each statistic category
    tasks_completed_label = Label(employee_root, text="Tasks Completed:")
    tasks_completed_label.pack()
    tasks_completed_value = Label(employee_root, text="")
    tasks_completed_value.pack()

    calls_taken_label = Label(employee_root, text="Calls Taken:")
    calls_taken_label.pack()
    calls_taken_value = Label(employee_root, text="")
    calls_taken_value.pack()

    # Add other labels as needed
    # ...

    # Start the main loop
    employee_root.mainloop()


# Call the employee_window function
employee_window()

