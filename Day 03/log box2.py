import tkinter as tk  # Import tkinter for GUI development
from tkinter import ttk  # Import ttk for themed widgets

# Create the main application window
root = tk.Tk()
root.title("Login")  # Set the title of the window
root.geometry("550x250")  # Set the size of the window
root.resizable(True, True)  # Allow resizing of the window

# Define a style for the button
style1 = ttk.Style()
style1.configure(
    "text.TButton",
    font=("Times New Roman", 20),  # Set the font for the button
    justify="center",
    foreground="black"
)

# Create a label for the username field
unLabel = ttk.Label(
    root,
    text="User Name: ",
    font=("Times New Roman", 20),
    justify="left"
)

# Create an entry widget for username input
unInput = ttk.Entry(
    root,
    font=("Times New Roman", 20),
    justify="center"
)

# Create a label for the password field
pwLabel = ttk.Label(
    root,
    text="Password: ",
    font=("Times New Roman", 20),
    justify="left"
)

# Create an entry widget for password input with obscured text
pwInput = ttk.Entry(
    root,
    font=("Times New Roman", 20),
    justify="center",
    show="*"  # Mask the input for the password field
)

# Create a Submit button
button1 = ttk.Button(
    root,
    text="Submit",  # Set button text
    width=10,
    style="text.TButton"
)

# Place widgets using a grid layout
unLabel.grid(row=1, column=2, padx=30, pady=(30, 10))  # Username label with padding
unInput.grid(row=1, column=3)  # Username input field
pwLabel.grid(row=2, column=2, pady=(30, 30))  # Password label with padding
pwInput.grid(row=2, column=3)  # Password input field
button1.grid(row=3, column=3, sticky=tk.W)  # Submit button aligned to the west (left)

# Start the Tkinter event loop
root.mainloop()
