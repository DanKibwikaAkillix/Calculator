from tkinter import Tk, Entry, Button, StringVar, Frame
from tkinter import PhotoImage

class Calculator:
    def __init__(self, master):
        master.title("Meiji")
        master.geometry('357x450+0+0')
        master.config(bg='#1e1e2e')
        master.resizable(False, False)

        try:
            icon = PhotoImage(file="image/logo.png")
            master.iconphoto(False, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        self.equation = StringVar()
        self.entry_value = ''

        Entry(
            master, width=22, bg='#2d2d3b', fg='white', font=('Arial Bold', 24),
            textvariable=self.equation, justify='right', bd=0, highlightthickness=0
        ).place(x=5, y=10, width=320, height=40)

        button_frame = Frame(master, bg='#1e1e2e')
        button_frame.place(x=10, y=80, width=337, height=360)

        buttons = [
            ('7', 0, 0), ('8', 1, 0), ('9', 2, 0), ('/', 3, 0),
            ('4', 0, 1), ('5', 1, 1), ('6', 2, 1), ('*', 3, 1),
            ('1', 0, 2), ('2', 1, 2), ('3', 2, 2), ('-', 3, 2),
            ('C', 0, 3), ('0', 1, 3), ('=', 2, 3), ('+', 3, 3),
        ]

        for (text, col, row) in buttons:
            Button(
                button_frame, text=text, width=5, height=2, font=('Arial', 14, 'bold'),
                fg='#fff', bg='#3b3b4f', activebackground='#575766', activeforeground='#fff',
                relief='flat', bd=0, command=lambda value=text: self.on_button_click(value)
            ).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "C":
            self.clear()
        elif value == "=":
            self.solve()
        else:
            self.show(value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
