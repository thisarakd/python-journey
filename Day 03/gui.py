import tkinter as tk  # Import the tkinter module for GUI development
from tkinter import ttk  # Import ttk for themed widgets
from tkinter import font  # Import font for custom font styling

# Create the main application window
root = tk.Tk()
root.title("GUI")  # Set the title of the window


# Function to center the window and create widgets
def center():
    width, height = 300, 500  # Desired width and height of the GUI window
    screen_width = root.winfo_screenwidth()  # Get the width of the screen
    screen_height = root.winfo_screenheight()  # Get the height of the screen
    x = int(screen_width / 2 - width / 2)  # Calculate x-coordinate for centering
    y = int(screen_height / 2 - height / 2)  # Calculate y-coordinate for centering
    root.geometry(f"{width}x{height}+{x}+{y}")  # Set the window geometry

    # String variable to bind with widgets
    text_var = tk.StringVar()
    text_var.set('test')  # Set an initial value

    # Define a custom font
    font1 = font.Font(family="Times New Roman", size=50, weight="bold")

    # Create a text entry field with custom font and styling
    user_name = ttk.Entry(
        root,
        width=50,
        foreground='red',
        font=font1,
        textvariable=text_var,
        justify="center"
    )

    # Create a label widget with the same text variable and font
    label = ttk.Label(
        root,
        foreground="blue",
        font=font1,
        textvariable=text_var
    )

    # Pack (place) the entry field and label on the window
    user_name.pack()
    label.pack()

    # Define a custom style for the button
    style1 = ttk.Style()
    style1.configure("text.TButton", font=("Arial", 18, "bold"), foreground="pink")

    # Function to print the value of `text_var` when the button is clicked
    def test():
        print(text_var.get())  # Output the text from the entry field to the console

    # Create a button and configure its properties
    button1 = ttk.Button(root, command=test)  # Assign the `test` function to the button
    button1.configure(text="Submit", style="text.TButton", width=7)
    button1.pack()


# Call the `center` function to set up the GUI
center()

# Allow resizing of the window
root.resizable(True, True)

# Start the Tkinter event loop
root.mainloop()
