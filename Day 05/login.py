import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.title("Login")


def center():
    width, height = 250, 100  # Desired width and height of the GUI window
    screen_width = root.winfo_screenwidth()  # Get the width of the screen
    screen_height = root.winfo_screenheight()  # Get the height of the screen
    x = int(screen_width / 2 - width / 2)  # Calculate x-coordinate for centering
    y = int(screen_height / 2 - height / 2)  # Calculate y-coordinate for centering
    root.geometry(f"{width}x{height}+{x}+{y}")


def login():
    u_name, pw, marks = u_input.get(), p_input.get(), int(m_input.get())
    if u_name == "":
        print("Please enter username")
    elif pw == "":
        print("Please enter password")
    elif marks == "":
        print("Please enter marks")
    else:
        if u_name == "Admin" and pw == "12345":
            print("Login Success")

            print("Grade A" if marks > 75 else "Grade B")
            # if marks > "75":
            #     print("Grade A")
            # elif marks > "65":
            #     print("Grade B")
            # elif marks > "50":
            #     print("Grade C")
            # elif marks > "40":
            #     print("Grade S")
            # else:
            #     print("You are Failed")
        elif u_name != "Admin" and pw != "12345":
            print("Incorrect Username and Password")
        elif u_name != "Admin":
            print("Incorrect Username")
        elif pw != "12345":
            print("Incorrect Password")


u_label = tk.Label(root, text="Username :")
p_label = tk.Label(root, text="Password :")
m_label = tk.Label(root, text="Marks :")
u_input = tk.Entry(root, width=20)
p_input = tk.Entry(root, width=20, show="*")
m_input = tk.Entry(root, width=20)
submit = tk.Button(root, text="Submit", command=login)

u_label.grid(row=0, column=0, pady=5)
u_input.grid(row=0, column=1, pady=5)
p_label.grid(row=1, column=0, pady=5)
p_input.grid(row=1, column=1, pady=5)
m_label.grid(row=2, column=0, pady=5)
m_input.grid(row=2, column=1, pady=5)
submit.grid(row=0, column=2, pady=5, padx=5)

center()
root.mainloop()
