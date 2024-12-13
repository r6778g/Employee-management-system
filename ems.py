from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
import database  # Import the database functions
from PIL import Image
# Function to refresh the TreeView data
def refresh_treeview():
    for i in tree.get_children():
        tree.delete(i)  # Clear existing data
    employees = database.fetch_employees()  # Fetch updated data
    for employee in employees:
        tree.insert('', 'end', values=employee)

# Function to handle adding new employees
def add_employee():
    name = nameEnter.get()
    phone = phoneEnter.get()
    role = roleBox.get()
    gender = genderBox.get()
    salary = salaryEnter.get()

    if not name or not phone or not role or not gender or not salary:
        messagebox.showerror('Error', 'Please fill all fields.')
    else:
        database.insert_employee(name, phone, role, gender, salary)
        refresh_treeview()

# Function to handle updating existing employees
def update_employee():
    selected = tree.focus()  # Get selected item in TreeView
    if not selected:
        messagebox.showerror('Error', 'Please select an employee to update.')
        return

    values = tree.item(selected, 'values')  # Get selected employee details
    emp_id = values[0]

    name = nameEnter.get()
    phone = phoneEnter.get()
    role = roleBox.get()
    gender = genderBox.get()
    salary = salaryEnter.get()

    if not name or not phone or not role or not gender or not salary:
        messagebox.showerror('Error', 'Please fill all fields.')
    else:
        database.update_employee(emp_id, name, phone, role, gender, salary)
        refresh_treeview()

# Function to handle deleting employees
def delete_employee():
    selected = tree.focus()  # Get selected item in TreeView
    if not selected:
        messagebox.showerror('Error', 'Please select an employee to delete.')
        return

    values = tree.item(selected, 'values')  # Get selected employee details
    emp_id = values[0]
    database.delete_employee(emp_id)
    refresh_treeview()

# GUI setup code...

window = CTk()
window.geometry('930x580')
window.title('Employment Management System')

# Load and display the image
image = CTkImage(Image.open('img_1.png'), size=(930, 180))
logo = CTkLabel(window, image=image, text='')
logo.grid(column=0, row=0, columnspan=2)

# Left Frame for Form Input
leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0)

nameLabel = CTkLabel(leftFrame, text='Employee Name', text_color='black')
nameLabel.grid(column=0, row=0)
nameEnter = CTkEntry(leftFrame)
nameEnter.grid(column=1, row=0)

phoneLabel = CTkLabel(leftFrame, text='Phone Number', text_color='black')
phoneLabel.grid(column=0, row=1)
phoneEnter = CTkEntry(leftFrame)
phoneEnter.grid(column=1, row=1)

roleLabel = CTkLabel(leftFrame, text='Role', text_color='black')
roleLabel.grid(column=0, row=2)
role_options = ['web developer', 'network engineer', 'business analyst', 'data scientist', 'UI/UX designer', 'technical writer']
roleBox = CTkComboBox(leftFrame, values=role_options)
roleBox.grid(column=1, row=2)

genderLabel = CTkLabel(leftFrame, text='Gender', text_color='black')
genderLabel.grid(column=0, row=3)
genderBox = CTkComboBox(leftFrame, values=['Male', 'Female'])
genderBox.grid(column=1, row=3)

salaryLabel = CTkLabel(leftFrame, text='Salary', text_color='black')
salaryLabel.grid(column=0, row=4)
salaryEnter = CTkEntry(leftFrame)
salaryEnter.grid(column=1, row=4)

# Right Frame for TreeView and Search
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)

search_option = ['id', 'name', 'phone', 'role', 'gender', 'salary']
searchbox = CTkComboBox(rightFrame, values=search_option)
searchbox.grid(column=1, row=0)
searchEntry = CTkEntry(rightFrame)
searchEntry.grid(column=2, row=0)
searchButton = CTkButton(rightFrame, text='Search')
searchButton.grid(column=3, row=0)
showallButton = CTkButton(rightFrame, text='Show All', command=refresh_treeview)
showallButton.grid(column=4, row=0)

# TreeView to display employee data
tree = ttk.Treeview(rightFrame, columns=('id', 'name', 'phone', 'role', 'gender', 'salary'), height=15)
tree.grid(column=1, row=1, columnspan=4)
tree['show'] = 'headings'  # Show headings

# Define column headings and column width
tree.heading('id', text='ID')
tree.heading('name', text='Name')
tree.heading('phone', text='Phone Number')
tree.heading('role', text='Role')
tree.heading('gender', text='Gender')
tree.heading('salary', text='Salary')

tree.column('id', width=50)
tree.column('name', width=100)
tree.column('phone', minwidth=100, width=100)
tree.column('role', minwidth=100, width=100)
tree.column('gender', minwidth=100, width=100)
tree.column('salary', minwidth=100, width=100)

# Add scrollbar to TreeView
scrollbar = ttk.Scrollbar(rightFrame, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(column=5, row=1, sticky='ns')

# Button Frame
buttonFrame = CTkFrame(window, fg_color='white')
buttonFrame.grid(row=2, column=0, columnspan=2)

addButton = CTkButton(buttonFrame, text='Add Employee', command=add_employee)
addButton.grid(column=0, row=0, padx=10, pady=10)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', command=delete_employee)
deleteButton.grid(column=1, row=0, padx=10, pady=10)

editButton = CTkButton(buttonFrame, text='Edit Employee', command=update_employee)
editButton.grid(column=2, row=0, padx=10, pady=10)

deleteallButton = CTkButton(buttonFrame, text='Delete All Employees')
deleteallButton.grid(column=3, row=0, padx=10, pady=10)

# Initialize TreeView with employee data
refresh_treeview()

window.mainloop()
