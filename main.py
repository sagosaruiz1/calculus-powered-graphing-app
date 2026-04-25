import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
import sympy as sp
import numpy as np

import calc_logic as calc
import visualizer as vslr

class CalculusApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculus-Powered Graphing App")
        self.root.geometry("450x400")
        self.root.configure(bg="#f4f4f9")

        tk.Label(root, text="Calculus Powered Grapher", 
                 font=("Helvetica", 16, "bold"), 
                 bg=("#f4f4f9"), 
                 fg="#333").pack(pady=15)
        
        tk.Label(root, text="Enter function (e.g., x**2 + 3*x + 5)", 
                 bg="#f4f4f9").pack()
        self.func_input = tk.Entry(root, width=15, font=("Courier", 10))
        self.func_input.insert(0, "x**2")
        self.func_input.pack(pady=5)

        tk.Label(root, text="X-Range (Start and End): ", bg='#f4f4f9').pack(pady=(10,0))
        range_frame = tk.Frame(root, bg='#f4f4f9')
        range_frame.pack(pady=5)

        self.start_x = tk.Entry(range_frame, width=8)
        self.start_x.insert(0, "-10")
        self.start_x.pack(side=tk.LEFT, padx=5)

        self.end_x = tk.Entry(range_frame, width=8)
        self.end_x.insert(0, "10")
        self.end_x.pack(side=tk.LEFT, padx=5)

        self.btn = tk.Button(root, text="Generate Graph & Data", command=self.process_data, 
                            bg='#2c3e50', fg='white', font=("Arial", 10, "bold"), 
                            padx=20, pady=10, cursor="hand2")
        self.btn.pack(pady=25)

        tk.Label(root, text="Project by: Ruiz Sagosa", 
                 font=("Arial", 8), bg='#f4f4f9', fg='#888')
        
    def process_data(self):

        try:
            user_func = self.func_input.get()
            x_min = float(self.start_x.get())
            x_max = float(self.end_x.get())

            x_sym = sp.symbols('x')
            expr = sp.sympify(user_func)

            f_numerical = sp.lambdify(x_sym, expr, 'numpy')

            x_values = np.linspace(x_min, x_max, 500)
            y_values = f_numerical(x_values)

            deriv_values = calc.get_derivative(f_numerical, x_values)
            total_area = calc.get_integral(f_numerical, x_min, x_max)

            res_fraction = Fraction(total_area).limit_denominator()
            messagebox.showinfo("Calculus Results", 
                                f"For f(x) = {user_func}\n\n"
                                f"Total Area (Integral) from {x_min} to {x_max}: \n"
                                f"Decimal: {total_area:.4f}\n"
                                f"Fraction (Approx): {res_fraction}")
            
            vslr.generate_plot(x_values, y_values, deriv_values, user_func)

        except Exception as e:
            messagebox.showerror("Math Error", f"\nCheck your Syntax!!!!!\n\nDetails: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculusApp(root)
    root.mainloop()
