"""Author:  Shanon Giles
Date written: 07/25/24
Assignment: Module 08 Final Project Submission
Short Desc: This Project displays a Tkinter application that will show metrics for three employees
and will the user to access their individual metrics for the month and as well any bonuses earned for the month.
There will also a user access for the supervisor to view the sum of metrics for all three employees.
Employees and Supervisors must provide an Access ID to view any metrics in the application. Once finish the user
can exit the application
"""
from tkinter import *  # Imports all widgets from tkinter library
from PIL import ImageTk, Image  # Imports functionalities for handling images

# Import messagebox for pop-up notifications
from tkinter import messagebox


class Employee:
    """
    This class defines an Employee object with attributes for name, department, and access ID.
    """

    def __init__(self, name, department, access_id):
        """
        Initializes an Employee object with the provided name, department, and access ID.

        Args:
            name (str): The employee's name.
            department (str): The employee's department.
            access_id (int): The employee's unique access ID.
        """

        self.name = name
        self.department = department
        self.access_id = access_id


# List of pre-defined Employee objects
EMPLOYEES = [
    Employee('Petter Townson', 'Customer Experience', 123904),
    Employee('Jessica Ivy', 'Engineering', 456112),
    Employee('Franklin Opal', 'Marketing', 711567)
]


# Main Tkinter Window Creation
root = Tk()  # Creates the main Tkinter window
root.title("Metro Facts Getting the numbers right, every time!")  # Sets the window title
root.iconbitmap('c:/gui/sgdiamond.ico')  # Sets the window icon (replace path if needed)
root.geometry("800x800")  # Sets the window size (800x800 pixels)

# Enables responsive window resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


# Main Menu Frame and Label Creation
title_frame = LabelFrame(root, text="Main Menu", fg="white", bg="green", width=100, height=100, relief=SUNKEN)
title_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
title_frame.grid_rowconfigure(0, weight=1)
title_frame.grid_columnconfigure(0, weight=1)

title_label = Label(master=title_frame, text="Metro Facts", fg="white", bg="gold4", width=25, height=15,
                    font=("Roboto", 12, "bold"), relief=RAISED)
title_label.grid(row=0, column=0, columnspan=2, padx=50, pady=50)  # Positions the label with padding


# "Close Window" Button
cls_btn1 = Button(root, text="Close Window", command=root.destroy).grid(row=8, column=0, padx=10, pady=10)


def show_bonus():
    """
    Displays a pop-up message congratulating the user on their bonus earnings.
    """
    messagebox.showinfo("Bonuses", "Congratulations! You've Earned $150.22 as of 7/27/24.")


def validate_employee(access_id):
    """
    Checks if the provided access ID is a valid integer (digits only).

    Args:
        access_id (str): The access ID entered by the user.

    Returns:
        bool: True if the access ID is valid (digits only), False otherwise.
    """

    if access_id.isdigit():
        return True
    else:
        return False


def on_invalid():
    """
    Displays a pop-up error message when an invalid access ID is entered.
    """
    messagebox.showerror("No Record Found", "Please enter a valid access ID.")



# Global variables (explained later in their respective functions)
global my_img
global entry_name
global entry_department
global entry_access_id


def open_emp_access():
    """
    This function opens a new window displaying employee metrics.
    """
    global my_img  # Used to store the image for the window

    # Create the new window
    top = Toplevel()
    top.title("Employee Metrics")
    top.iconbitmap('c:/gui/sgdiamond.ico')

    # Load and display the image
    my_img = ImageTk.PhotoImage(Image.open('c:/metro facts/fact python image.png'))
    Label(top, image=my_img).grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Create labels and variables for employee metrics
    tasks_completed = IntVar()
    tasks_completed_label = Label(top, text="Tasks Completed:")
    tasks_completed_label.grid(row=2, column=0, sticky='w')
    tasks_completed_value = Label(top, textvariable=tasks_completed)
    tasks_completed_value.grid(row=2, column=1, sticky='e')

    calls_taken = IntVar()
    calls_taken_label = Label(top, text="Calls Taken:")
    calls_taken_label.grid(row=3, column=0, sticky='w')
    calls_taken_value = Label(top, textvariable=calls_taken)
    calls_taken_value.grid(row=3, column=1, sticky='e')

    products_sold = IntVar()
    products_sold_label = Label(top, text="Products Sold:")
    products_sold_label.grid(row=4, column=0, sticky='w')
    products_sold_value = Label(top, textvariable=products_sold)
    products_sold_value.grid(row=4, column=1, sticky='e')

    task_errors = IntVar()
    task_errors_label = Label(top, text="Task Errors:")
    task_errors_label.grid(row=5, column=0, sticky='w')
    task_errors_value = Label(top, textvariable=task_errors)
    task_errors_value.grid(row=5, column=1, sticky='e')

    # Set initial values for the metrics
    tasks_completed.set(1000)
    calls_taken.set(400)
    products_sold.set(200)
    task_errors.set(15)

    # Configure window resizing
    top.grid_rowconfigure(0, weight=1)
    top.grid_columnconfigure(0, weight=1)

    # Close button
    Button(top, text="Close Window", command=top.destroy).grid(row=8, column=0, padx=10, pady=10)

    # Bonus button (command not provided)
    Button(top, text="See Bonus Earnings", command=show_bonus).grid(row=9, column=0, padx=10, pady=10)


def on_access_metrics():
    """
    This function checks if the entered ID is valid and opens the employee metrics window if so.
    """
    if validate_employee(entry_access_id.get()):  # Call validation function (not shown)
        open_emp_access()
    else:
        on_invalid()  # Call function to handle invalid ID (not shown)



# This function opens a new window titled "Employee Page" for employee access functionalities.

def open_employee():
    """
    This function opens a new window for employee access functionalities.
    """

    global my_img  # Declare global variable to hold the image for the window
    global entry_name  # Declare global variable to hold the entry widget for name (not currently used)
    global entry_department  # Declare global variable to hold the entry widget for department (not currently used)
    global entry_access_id  # Declare global variable to hold the entry widget for access ID

    # Create a new top-level window
    top = Toplevel()
    top.title("Employee Page")  # Set the title of the window

    # Set the window icon (path needs adjustment if image location changes)
    top.iconbitmap('c:/gui/sgdiamond.ico')

    # Load the image for the window background
    my_img = ImageTk.PhotoImage(Image.open('c:/metro facts/fact python image.png'))

    # Create a label to display the image and fill the first row and all columns
    Label(top, image=my_img).grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Register validation functions for the access ID entry
    validate_step1 = (top.register(validate_employee), '%P')  # Function for validation
    validate_step2 = (top.register(on_invalid),)  # Function for handling invalid input

    # Configure grid row and column weights for responsiveness
    top.grid_rowconfigure(0, weight=1)
    top.grid_columnconfigure(0, weight=1)

    # (These lines seem commented out, but are included for completeness)
    # title_frame.grid_rowconfigure(0, weight=1)
    # title_frame.grid_columnconfigure(0, weight=1)

    # Create a button to close the window
    cls_btn2 = Button(top, text="Close Window", command=top.destroy).grid(row=8, column=0, padx=10, pady=10)

    # Create a label for the access ID entry
    label_access_id = Label(top, text="Enter your Access ID")
    label_access_id.grid(row=1, column=0, padx=10, pady=10)

    # Create an entry widget for access ID with validation
    entry_access_id = Entry(top, validate="focusout", validatecommand=validate_step1, invalidcommand=validate_step2)
    entry_access_id.insert(0, "Enter Access ID")  # Set default text for the entry
    entry_access_id.grid(row=2, column=0, padx=10, pady=10)

    # Create a button for accessing employee metrics (function not defined)
    access_emp_button = Button(top, text="Access Metrics", fg="gold", bg="green", font=("Roboto", 12, "bold"),
                               command=on_access_metrics).grid(row=7, column=0, padx=10, pady=10)


# Create a frame for the employee access button (potentially for styling)
frame_emp_button = Frame(root, bg="green", width=100, height=100, relief=SUNKEN)
frame_emp_button.grid(row=2, column=0, columnspan=3, sticky="ew")
frame_emp_button.grid_rowconfigure(0, weight=1)
frame_emp_button.grid_columnconfigure(0, weight=1)

# Create the main employee access button with styling and functionality
emp_button = Button(frame_emp_button, text="Employee Access", width=25, height=5, bg="green", fg="white",
                    font=("Roboto", 12),
                    relief=RAISED, command=open_employee).grid(row=0, column=0, padx=50, pady=50)

# Start the main event loop for the application
root.mainloop()
