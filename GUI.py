import tkinter as tk  # Import the tkinter module for GUI development

# Create the main application window
root = tk.Tk()

# Disable the resizing of the window
root.resizable(False, False)

# Set the title of the application window
root.title("GUI")


# Define a function to center the window on the screen
def center():
    width = 500  # Desired width of the GUI window
    height = 800  # Desired height of the GUI window

    # Get the screen's width and height
    s_width = root.winfo_screenwidth()  # Get the width of the screen
    s_height = root.winfo_screenheight()  # Get the height of the screen

    # Calculate the x and y coordinates to position the window at the center
    x = int(s_width / 2 - width / 2)  # Horizontal position: center of the screen
    y = int(s_height / 2 - height / 2)  # Vertical position: center of the screen

    # Set the window's geometry to the calculated size and position
    root.geometry(f"{width}x{height}+{x}+{y}")


# Call the center function to center the window on the screen
center()

# Start the Tkinter event loop
root.mainloop()
