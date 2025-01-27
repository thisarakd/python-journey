import tkinter as tk
from tkinter import  messagebox

root = tk.Tk()
root.resizable(False, False)
root.title("Gender Selection")
root.geometry("150x150")


def output():
    gender = "Male" if selected_gender.get() == 1 else "Female"
    messagebox.showinfo('Gender', f'Selected gender is {gender}')


selected_gender = tk.IntVar()
selected_gender.set(1)


male_btn = tk.Radiobutton(root, text="Male", variable=selected_gender, value=1)
female_btn = tk.Radiobutton(root, text="Female", variable=selected_gender, value=0)
submit = tk.Button(root, text="Submit")

male_btn.grid(row=0, column=0)
female_btn.grid(row=0, column=1)
submit.grid(row=1, columnspan=2)
root.mainloop()