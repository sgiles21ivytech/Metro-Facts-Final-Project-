""" This is the first portion of the Metro facts where stats are displayed in
 Gui"""

# This will import all tkinter functions
from tkinter import *

# Will cause the terminal to display a window with a title and logo icon
root = Tk()
root.title("Metro Facts Getting the numbers right, every time!")
root.iconbitmap('c:/gui/sgdiamond.ico')

# Titles will display with in certain row and columns with font adjustments
title_label = Label(root, text="Stats", font=("Roboto", 12, "bold"))
title_label.grid(row=1, column=0, padx=50, pady=50)
value_label = Label(root, text="Total for the Month", font=("Roboto", 12, "bold"))
value_label.grid(row=1, column=1, padx=50, pady=50)

"Below are individual stats by category"

# Tasks completed
tasks_completed = IntVar()
tasks_completed_label = Label(root, text="Tasks Completed:")
tasks_completed_label.grid(row=2, column=0)
tasks_completed_value = Label(root, textvariable=tasks_completed)
tasks_completed_value.grid(row=2, column=1)

# Calls taken
calls_taken = IntVar()
calls_taken_label = Label(root, text="Calls Taken:")
calls_taken_label.grid(row=3, column=0)
calls_taken_value = Label(root, textvariable=calls_taken)
calls_taken_value.grid(row=3, column=1)

# Products sold
products_sold = IntVar()
products_sold_label = Label(root, text="Products Sold:")
products_sold_label.grid(row=4, column=0)
products_sold_value = Label(root, textvariable=products_sold)
products_sold_value.grid(row=4, column=1)

# Number of errors
task_errors = IntVar()
task_errors_label = Label(root, text="Task Errors:")
task_errors_label.grid(row=5, column=0)
task_errors_value = Label(root, textvariable=task_errors)
task_errors_value.grid(row=5, column=1)

# Monthly total set to each Label
tasks_completed.set(1000)
calls_taken.set(400)
products_sold.set(200)
task_errors.set(15)

# This will keep the program running as long as the Gui window stays open.
root.mainloop()
