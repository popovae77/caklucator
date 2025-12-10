import tkinter as tk
from tkinter import messagebox
from calc import Calc
from memory import Mem
import math
calc = Calc()
mem = Mem()
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("420x580")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, bg="#f4f4f4")
        input_frame.pack(pady=20)

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=('Segoe UI', 24, 'bold'),
            width=17,
            bd=4,
            relief='flat',
            bg="#ffffff",
            justify='right',
            fg="#333333"
        )
        input_field.grid(row=0, column=0, ipady=15)
        input_field.focus_set()

        self.create_buttons()

    def create_buttons(self):
        btns_frame = tk.Frame(self.root, bg="#f4f4f4")
        btns_frame.pack()

        button_style = {
            "font": ('Segoe UI', 14, 'bold'),
            "bd": 0,
            "width": 6,
            "height": 2,
            "relief": "ridge"
        }

        buttons = [
            ['7', '8', '9', '/', 'sin'],
            ['4', '5', '6', '*', 'cos'],
            ['1', '2', '3', '-', '√'],
            ['0', '.', '=', '+', '^'],
            ['%', 'floor', 'ceil', 'M+', 'M-'],
            ['MR', 'MC', 'C']
        ]

        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                color_bg = "#ffffff"
                color_fg = "#333333"

                if btn_text in ['=', 'C']:
                    color_bg = "#2196F3"
                    color_fg = "white"
                elif btn_text in ['+', '-', '*', '/', '^', '%']:
                    color_bg = "#90CAF9"
                elif btn_text in ['sin', 'cos', '√', 'floor', 'ceil']:
                    color_bg = "#C5E1A5"
                elif btn_text.startswith("M"):
                    color_bg = "#FFE082"

                tk.Button(
                    btns_frame,
                    text=btn_text,
                    bg=color_bg,
                    fg=color_fg,
                    activebackground="#eeeeee",
                    activeforeground="#000000",
                    command=lambda text=btn_text: self.on_button_click(text),
                    **button_style
                ).grid(row=r, column=c, padx=5, pady=5)

    def on_button_click(self, char):
        try:
            if char == "C":
                self.expression = ""
                self.input_text.set("")
            elif char == "=":
                self.evaluate_expression()
            elif char == "√":
                value = float(self.input_text.get())
                result = calc.square_root(value)
                self.update_display(result)
            elif char == "sin":
                value = float(self.input_text.get())
                result = calc.sin(value)
                self.update_display(result)
            elif char == "cos":
                value = float(self.input_text.get())
                result = calc.cos(value)
                self.update_display(result)
            elif char == "floor":
                value = float(self.input_text.get())
                result = calc.floor(value)
                self.update_display(result)
            elif char == "ceil":
                value = float(self.input_text.get())
                result = calc.rounding_up(value)
                self.update_display(result)
            elif char == "M+":
                if self.input_text.get():
                    mem.mem_add(float(self.input_text.get()))
            elif char == "M-":
                if self.input_text.get():
                    mem.mem_sub(float(self.input_text.get()))
            elif char == "MC":
                mem.mem_clear()
            elif char == "MR":
                mem = calc.mem_read()
                self.update_display(mem)
            elif char == "^":
                self.expression += "**"
                self.input_text.set(self.expression)
            else:
                self.expression += str(char)
                self.input_text.set(self.expression)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            self.expression = ""

    def evaluate_expression(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {
                "math": math,
                "sin": calc.sin,
                "cos": calc.cos,
                "sqrt": calc.square_root,
                "pow": pow
            })
            self.update_display(result)
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")
            self.expression = ""

    def update_display(self, value):
        """Обновляет поле ввода и выражение"""
        self.input_text.set(str(value))
        self.expression = str(value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
