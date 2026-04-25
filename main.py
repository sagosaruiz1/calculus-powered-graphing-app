import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
from fractions import Fraction

import calc_logic as calc
import visualizer as vslr


class CalculusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculus-Powered Graphing App")
        self.root.geometry("450x500")
        self.root.configure(bg='#f4f4f9')

        tk.Label(root, text="Calculus-Powered Graphing App",
                font=("Arial", 14, "bold"), 
                bg='#f4f4f9').pack(pady=10)
        
        tk.Label(root, text="Select Mode:", bg='#f4f4f9').pack()
        self.mode_var = tk.StringVar(root)
        self.mode_var.set("Area Under Curve")
        self.mode_menu = tk.OptionMenu(root, self.mode_var, "Area Under Curve", "Between Curves", command=self.toggle_inputs)
        self.mode_menu.pack(pady=5)

        tk.Label(root, text="function f(x):", bg="#f4f4f9").pack()
        self.f1_input = tk.Entry(root, width=30)
        self.f1_input.insert(0, '0')
        self.f1_input.pack()

        self.f2_label = tk.Label(root, text="function g(x):", bg='#f4f4f9')
        self.f2_input = tk.Entry(root, width=30)

        tk.Label(root, text="x range (Start, End):", bg='#f4f4f9').pack(pady=5)
        self.range_frame = tk.Frame(root, bg='#f4f4f9')
        self.range_frame.pack()

        self.start_x = tk.Entry(self.range_frame, width=10)
        self.start_x.insert(0, '0')
        self.start_x.pack(side=tk.LEFT)

        self.end_x = tk.Entry(self.range_frame, width=10)
        self.end_x.insert(0, '0')
        self.end_x.pack(side=tk.LEFT)

        self.btn = tk.Button(root, text="Calculate & Plot", command=self.process_data, 
                             bg='#2c3e50', fg="white", pady=10)
        self.btn.pack(pady=20)


    def toggle_inputs(self, selection):
        if selection == "Between Curves":
            self.f2_label.pack()
            self.f2_input.pack()
        else:
            self.f2_label.pack_forget()
            self.f2_input.pack_forget()


    def process_data(self):
        try:
            x_symbols = sp.symbols('x')
            f_sym = sp.sympify(self.f1_input.get())
            df_sym = sp.diff(f_sym, x_symbols)
            df_str = str(df_sym)
            f1_expr = sp.lambdify(x_symbols, sp.sympify(self.f1_input.get()), 'numpy')

            mode = self.mode_var.get()
            if mode == "Between Curves":
                f2_expr = sp.lambdify(x_symbols, sp.sympify(self.f2_input.get()), 'numpy')
                f2_str = self.f2_input.get()
            else:
                f2_expr = lambda x: np.zeros_like(x)
                f2_str = '0'

            x_min, x_max = float(self.start_x.get()), float (self.end_x.get())
            x_values = np.linspace(x_min, x_max, 500)

            y1_values = f1_expr(x_values)
            y2_values = f2_expr(x_values)
            deriv = calc.get_derivative(f1_expr, x_values)
            area = calc.get_integral(f1_expr, f2_expr, x_min, x_max)
            fraction_area = Fraction(area).limit_denominator(1000)
            df_sym = sp.diff(sp.sympify(self.f1_input.get()), sp.symbols('x'))
            df_sym = str(df_sym)
            pretty_df = df_sym.replace("**", "^").replace("*", "")

            messagebox.showinfo("Result",
                                f"Calculated Area:\n\n"
                                f"Decimal: {area:.4f}\n"
                                f"Fraction: {fraction_area}\n\n"
                                f"Derivative Formula:\n"
                                f"f'(x) = {pretty_df}")
            
            vslr.generate_plot(x_values, y1_values, y2_values, deriv, self.f1_input.get(), f2_str, mode, df_str)

        except Exception as e:
            messagebox.showerror("Error", f"WRONG SYNTAX!!!!\n\nInvalid input {e}")


if __name__ == "__main__":
    root = tk.Tk()
    logo = tk.PhotoImage(file='logo\calculus_logo.png')
    root.wm_iconphoto(False, logo)
    app = CalculusApp(root)
    root.mainloop()