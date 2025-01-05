import tkinter as tk  # Import tkinter for GUI development
from tkinter import ttk  # Import ttk for themed widgets
from tkinter import font  # Import font for custom font styling

# Create the main application window
root = tk.Tk()
root.title("GUI")  # Set the title of the window
root.geometry("400x300")  # Set the initial size of the window
root.resizable(True, True)  # Allow resizing of the window

# Initialize StringVar variables for dynamic text
login = tk.StringVar()
login.set('Log In')  # Set default text for the main label
unLabel = tk.StringVar()
unLabel.set('User Name')  # Set label text for username
pwLabel = tk.StringVar()
pwLabel.set('Password')  # Set label text for password
un = tk.StringVar()
un.set('')  # Set an initial empty value for the username input
pw = tk.StringVar()
pw.set('')  # Set an initial empty value for the password input

# Configure a style for the button
style1 = ttk.Style()
style1.configure("text.TButton", font=("Arial", 18, "bold"), foreground="black")  # Fixed typo in "foreground"

# Define a custom font for labels and entry fields
font1 = font.Font(family="Times New Roman", size=20, weight="bold")

# Create and configure widgets
label1 = ttk.Label(root, foreground="black", font=font1, textvariable=login)  # Main login label
unLabel1 = ttk.Label(root, foreground="black", font=font1, textvariable=unLabel, justify="right")  # Username label
pwLabel1 = ttk.Label(root, foreground="black", font=font1, textvariable=pwLabel, justify="right")  # Password label
unInput = ttk.Entry(root, width=50, foreground='black', font=font1, textvariable=un, justify="right")  # Username input field
pwInput = ttk.Entry(root, width=50, foreground='black', show="*", font=font1, textvariable=pw, justify="right")  # Password input field


# Define the check function to validate inputs
def check():
    # Check if the username matches "root"
    if un.get() == "root":
        unInput.configure(foreground="green")  # Change input text to green if correct
    else:
        unInput.configure(foreground="red")  # Change input text to red if incorrect

    # Check if the password matches "pass"
    if pw.get() == "pass":
        pwInput.configure(foreground="green")  # Change input text to green if correct
    else:
        pwInput.configure(foreground="red")  # Change input text to red if incorrect


# Create and configure the Submit button
button1 = ttk.Button(root, width=10, style="text.TButton", command=check, text="Submit")

# Pack widgets to add them to the window
label1.pack()  # Main login label
unLabel1.pack()  # Username label
unInput.pack()  # Username input field
pwLabel1.pack()  # Password label
pwInput.pack()  # Password input field
button1.pack()  # Submit button

# Start the Tkinter event loop
root.mainloop()
