import tkinter as tk
from tkinter import messagebox


class Call:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Cal")
        self.root.resizable(False, False)
        self.create_compornent()

    def is_operator(self, value):
        if value == "+" or value == "-" or value == "/" or value == "X":
            return True
        else:
            return False

    def has_a_period(self, value):
        chars = ['+', '-', 'x', '/', '(', ')']
        for ch in chars:
            value = value.replace(ch, '@')
        parts = value.split('@')
        last_value = parts[len(parts) - 1]
        #print(last_value)
        if '.' in last_value:
            return True
        else:
            return False

    def add_text_to_display(self, text):
        value = self.text.get()
        if (value == "0" and text != "." and not self.is_operator(text)):
            value = ""
        elif text == "." and self.has_a_period(value):
            text = ""

        if (text == "C"):
            self.text.set("0")
        elif text == "CE":
            self.text.set(value[:-1])
            if self.text.get() == "":
                self.text.set("0")
        elif self.is_operator(text) and self.is_operator(value[-1:]):
            self.text.set(value[:-1] + text)
        else:
            self.text.set(value + text)

    def result(self):
        try:
            value = self.text.get().replace('X', '*')
            result = eval(value)
            self.text.set(result)
        except Exception as e:
            messagebox.showerror("Invalid Operator", "Enter Valid Operator!")

    def create_compornent(self):
        self.text = tk.StringVar()
        self.text.set("0")
        self.display = tk.Entry(self.root, justify="right", font=('Arial', 25, "bold"), state="readonly",
                                textvariable=self.text)
        self.display.grid(column=0, row=0, columnspan=4, padx=5, pady=5)

        #but row 1
        bt_back1 = tk.Button(self.root, text="(", font=('Arial', 25, "bold"), width=2, height=2, fg="blue",
                             command=lambda: self.add_text_to_display("("))
        bt_back1.grid(column=0, row=1, padx=5, pady=5)

        bt_back2 = tk.Button(self.root, text=")", font=('Arial', 25, "bold"), width=2, height=2, fg="blue",
                             command=lambda: self.add_text_to_display(")"))
        bt_back2.grid(column=1, row=1, padx=5, pady=5)

        bt_c = tk.Button(self.root, text="C", font=('Arial', 25, "bold"), width=2, height=2, fg="blue",
                         command=lambda: self.add_text_to_display("C"))
        bt_c.grid(column=2, row=1, padx=5, pady=5)

        bt_ce = tk.Button(self.root, text="CE", font=('Arial', 25, "bold"), width=2, height=2, fg="blue",
                          command=lambda: self.add_text_to_display("CE"))
        bt_ce.grid(column=3, row=1, padx=5, pady=5)
        #but row 2
        bt_7 = tk.Button(self.root, text="7", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("7"))
        bt_7.grid(column=0, row=2, padx=5, pady=5)

        bt_8 = tk.Button(self.root, text="8", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("8"))
        bt_8.grid(column=1, row=2, padx=5, pady=5)

        bt_9 = tk.Button(self.root, text="9", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("9"))
        bt_9.grid(column=2, row=2, padx=5, pady=5)

        bt_div = tk.Button(self.root, text="/", font=('Arial', 25, "bold"), width=2, height=2, fg="red",
                           command=lambda: self.add_text_to_display("/"))
        bt_div.grid(column=3, row=2, padx=5, pady=5)

        # but row 3
        bt_4 = tk.Button(self.root, text="4", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("4"))
        bt_4.grid(column=0, row=3, padx=5, pady=5)

        bt_5 = tk.Button(self.root, text="5", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("5"))
        bt_5.grid(column=1, row=3, padx=5, pady=5)

        bt_6 = tk.Button(self.root, text="6", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("6"))
        bt_6.grid(column=2, row=3, padx=5, pady=5)

        bt_mul = tk.Button(self.root, text="X", font=('Arial', 25, "bold"), width=2, height=2, fg="red",
                           command=lambda: self.add_text_to_display("X"))
        bt_mul.grid(column=3, row=3, padx=5, pady=5)

        # but row 4
        bt_1 = tk.Button(self.root, text="1", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("1"))
        bt_1.grid(column=0, row=4, padx=5, pady=5)

        bt_2 = tk.Button(self.root, text="2", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("2"))
        bt_2.grid(column=1, row=4, padx=5, pady=5)

        bt_3 = tk.Button(self.root, text="3", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("3"))
        bt_3.grid(column=2, row=4, padx=5, pady=5)

        bt_mul = tk.Button(self.root, text="-", font=('Arial', 25, "bold"), width=2, height=2, fg="red",
                           command=lambda: self.add_text_to_display("-"))
        bt_mul.grid(column=3, row=4, padx=5, pady=5)

        # but row 5
        bt_dot = tk.Button(self.root, text=".", font=('Arial', 25, "bold"), width=2, height=2,
                           command=lambda: self.add_text_to_display("."))
        bt_dot.grid(column=0, row=5, padx=5, pady=5)

        bt_0 = tk.Button(self.root, text="0", font=('Arial', 25, "bold"), width=2, height=2,
                         command=lambda: self.add_text_to_display("0"))
        bt_0.grid(column=1, row=5, padx=5, pady=5)

        bt_00 = tk.Button(self.root, text="00", font=('Arial', 25, "bold"), width=2, height=2,
                          command=lambda: self.add_text_to_display("00"))
        bt_00.grid(column=2, row=5, padx=5, pady=5)

        bt_mul = tk.Button(self.root, text="+", font=('Arial', 25, "bold"), width=2, height=2, fg="red",
                           command=lambda: self.add_text_to_display("+"))
        bt_mul.grid(column=3, row=5, padx=5, pady=5)

        bt_mul = tk.Button(self.root, text="=", font=('Arial', 25, "bold"), width=18, height=2, fg="red",
                           command=self.result)
        bt_mul.grid(column=0, row=6, padx=5, columnspan=4, pady=5)

    def run(self):
        self.root.mainloop()


if __name__ == "_main_":
    c = Call()
    c.run()
