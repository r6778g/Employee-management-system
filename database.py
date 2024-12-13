import pymysql
from tkinter import messagebox

# Establish database connection and create tables if not present
def database_connect():
    try:
        connection = pymysql.connect(host='localhost', user='root', passwd='12345678')
        mycursor = connection.cursor()

        # Create database and table
        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
        mycursor.execute('USE employee_data')
        mycursor.execute('''CREATE TABLE IF NOT EXISTS data (
                                id INT PRIMARY KEY AUTO_INCREMENT, 
                                name VARCHAR(20), 
                                phone VARCHAR(20), 
                                role VARCHAR(20), 
                                gender VARCHAR(10),
                                salary DECIMAL(10,2))''')
        connection.commit()
        mycursor.close()
        connection.close()
    except pymysql.Error as e:
        messagebox.showerror('Database Error', f'Error: {e}')

# Insert employee record
def insert_employee(name, phone, role, gender, salary):
    try:
        connection = pymysql.connect(host='localhost', user='root', passwd='12345678', database='employee_data')
        mycursor = connection.cursor()
        mycursor.execute('INSERT INTO data (name, phone, role, gender, salary) VALUES (%s, %s, %s, %s, %s)',
                         (name, phone, role, gender, salary))
        connection.commit()
        mycursor.close()
        connection.close()
        messagebox.showinfo('Success', 'Employee added successfully.')
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Failed to insert employee: {e}')

# Fetch all employees
def fetch_employees():
    try:
        connection = pymysql.connect(host='localhost', user='root', passwd='12345678', database='employee_data')
        mycursor = connection.cursor()
        mycursor.execute('SELECT * FROM data')
        result = mycursor.fetchall()
        mycursor.close()
        connection.close()
        return result
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Failed to fetch employees: {e}')
        return []

# Update employee details
def update_employee(emp_id, name, phone, role, gender, salary):
    try:
        connection = pymysql.connect(host='localhost', user='root', passwd='12345678', database='employee_data')
        mycursor = connection.cursor()
        query = '''UPDATE data 
                   SET name=%s, phone=%s, role=%s, gender=%s, salary=%s 
                   WHERE id=%s'''
        mycursor.execute(query, (name, phone, role, gender, salary, emp_id))
        connection.commit()
        mycursor.close()
        connection.close()
        messagebox.showinfo('Success', 'Employee updated successfully.')
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Failed to update employee: {e}')

# Delete employee record by ID
def delete_employee(emp_id):
    try:
        connection = pymysql.connect(host='localhost', user='root', passwd='12345678', database='employee_data')
        mycursor = connection.cursor()
        mycursor.execute('DELETE FROM data WHERE id=%s', (emp_id,))
        connection.commit()
        mycursor.close()
        connection.close()
        messagebox.showinfo('Success', 'Employee deleted successfully.')
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Failed to delete employee: {e}')
