import numpy as np
from scipy.integrate import quad



def get_derivative(f, x_vals, dx=1e-6):

    return (f(x_vals + dx) - f(x_vals)) / dx

def get_integral(f1, f2, start, end):
  
    diff_func = lambda x: abs(f1(x) - f2(x))
    area, error = quad(diff_func, start, end)
    return area