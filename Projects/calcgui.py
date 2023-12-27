import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        # Entry widget to display the input and results
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.entry_var.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set('Error')
        else:
            new_text = current_text + button
            self.entry_var.set(new_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
