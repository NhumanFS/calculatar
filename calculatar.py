import tkinter as tk

color1 = "#7a7d87"
color2 = "#4b505c"
color3 = "#4b505c"
color4 = "#dedcf7"

LARGE_FONT_STYLE = ("Arial", 24, "bold")

DIS_FONT_STYLE = ("Arial", 40, "bold")

TOTAL_FONT_STYLE = ("Arial", 20, "bold")


class Calculatar:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("calculatar")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = ""
        self.current_expression = ""
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 1), ".": (4, 2)}
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_digitbuttons()
        self.create_operatorbuttos()
        self.create_sqrtbutton()
        self.create_sqrbutton()
        self.create_clearbutton()
        self.create_equal()
        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)
        self.total_label, self.label = self.create_displaylabel()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digitbuttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(
                digit), bg=color4, font=LARGE_FONT_STYLE, command=lambda x=digit: self.addexpresion(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=tk.NSEW)

    def create_operatorbuttos(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               bg=color4, font=LARGE_FONT_STYLE, command=lambda x=operator: self.addoperator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.updatelabel()

    def create_sqrtbutton(self):
        button = tk.Button(self.buttons_frame, text="\u221ax",
                           bg=color4, font=LARGE_FONT_STYLE, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def sqr(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.updatelabel()

    def create_sqrbutton(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2",
                           bg=color4, font=LARGE_FONT_STYLE, command=self.sqr)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.updatelabel()
        self.updatetotallabel()

    def create_clearbutton(self):
        button = tk.Button(self.buttons_frame, text="C",
                           bg=color3, font=LARGE_FONT_STYLE, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equal(self):
        button = tk.Button(self.buttons_frame, text="=",
                           bg=color3, font=LARGE_FONT_STYLE, command=self.equal)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def equal(self):
        self.total_expression += self.current_expression
        self.updatetotallabel()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception:
            self.current_expression = "ERROR"
        finally:
            self.updatelabel()

    def create_displaylabel(self):
        total_label = tk.Label(
            self.display_frame, text=self.total_expression, bg=color1, font=TOTAL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(
            self.display_frame, text=self.current_expression, bg=color1, font=DIS_FONT_STYLE)
        label.pack(expand=True, fill="both")
        return total_label, label

    def addexpresion(self, value):
        self.current_expression += str(value)
        self.updatelabel()

    def addoperator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.updatelabel()
        self.updatetotallabel()

    def updatetotallabel(self):
        expression = self.total_expression
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f"{symbol}")
        self.total_label.config(text=expression)

    def updatelabel(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


cal = Calculatar()
cal.run()
