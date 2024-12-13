from tkinter import messagebox
from customtkinter import *
from PIL import Image

# Define login function
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if username == '' or password == '':
        messagebox.showinfo("Error", "Please enter your username and password")
    elif username == 'mohit' and password == '123':
        messagebox.showinfo('Success', 'Login successful')
        root.destroy()
        import  ems
    else:
        messagebox.showinfo("Error", "Incorrect username or password")

# Create root window
root = CTk()
root.geometry("1400x900")
root.title("Login Page")

# Add background image
image = CTkImage(Image.open('img.png'), size=(1400, 900))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

# Add heading label
headingLabel = CTkLabel(root, text='Employee Management System', font=('Times New Roman', 35))
headingLabel.place(x=250, y=50)

# Add username and password labels
usernameLabel = CTkLabel(root, text='Username:', font=('Arial', 15))
usernameLabel.place(x=150, y=100)
usernameEntry = CTkEntry(root)
usernameEntry.place(x=250, y=100)

passwordLabel = CTkLabel(root, text='Password:', font=('Arial', 15))
passwordLabel.place(x=150, y=150)
passwordEntry = CTkEntry(root, show='*')
passwordEntry.place(x=250, y=150)

# Add login button
loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=250, y=200)

# Run the main loop
root.mainloop()
