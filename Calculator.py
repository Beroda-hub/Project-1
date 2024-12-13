import tkinter as tk
import math
from tkinter import Entry, Button, Tk

class SimpleCalculator:
    def __init__(self, master: Tk) -> None:
        """
        Initializes the SimpleCalculator application.

        Args:
            master (Tk): The root window for the calculator.
        """
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)  # Prevent resizing

        # Input field
        self.input_field: Entry = tk.Entry(
            master, font=("Arial", 24), width=14, bd=10, relief="sunken", justify="right"
        )
        self.input_field.grid(row=0, column=0, columnspan=4)
        self.input_field.insert(0, "0")

        # Buttons
        buttons: list[str] = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "\u221A", "C", "+/-", "x²"
        ]

        row: int = 1
        col: int = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            Button(master, text=button, width=4, height=2, command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button: str) -> None:
        """
        Handles button click events for the calculator.

        Args:
            button (str): The button label that was clicked.
        """
        if button == "C":
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, "0")
        elif button == "=":
            try:
                result = eval(self.input_field.get())
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, str(result))
            except Exception:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == "\u221A":  # Square root
            try:
                result = math.sqrt(float(self.input_field.get()))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, str(result))
            except Exception:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == "+/-":
            try:
                result = -float(self.input_field.get())
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, str(result))
            except Exception:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == "x²":  # Square
            try:
                result = float(self.input_field.get()) ** 2
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, str(result))
            except Exception:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        else:
            current = self.input_field.get()
            if current == "0":
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, button)
            else:
                self.input_field.insert(tk.END, button)

if __name__ == "__main__":
    root: Tk = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
