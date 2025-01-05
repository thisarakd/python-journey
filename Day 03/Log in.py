import tkinter as tk  # Import tkinter for GUI development
from tkinter import messagebox  # Import messagebox for displaying popup dialogs


# Define the login function
def login():
    # Get the values entered in the username and password fields
    username = entry_username.get()
    password = entry_password.get()

    # Authentication logic (customize this for your needs)
    if username == "admin" and password == "password":  # Correct username and password
        messagebox.showinfo("Login Successful", "Welcome!")  # Show success message
        root.destroy()  # Close the login dialog upon successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")  # Show error message


# Create the main application window
root = tk.Tk()
root.title("Login Dialog")  # Set the title of the window

# Create and place the username label and entry field
label_username = tk.Label(root, text="Username:")  # Label for username
label_username.pack(pady=5)  # Add vertical padding between widgets

entry_username = tk.Entry(root)  # Entry field for username
entry_username.pack(pady=5)

# Create and place the password label and entry field
label_password = tk.Label(root, text="Password:")  # Label for password
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")  # Entry field for password with masked input
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)  # Button to trigger login function
button_login.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
