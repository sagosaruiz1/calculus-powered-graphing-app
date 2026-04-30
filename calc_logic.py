import numpy as np
from scipy.integrate import quad



def get_derivative(f, x_values, dx=1e-6):

    return (f(x_values + dx) - f(x_values)) / dx

def get_integral(f1, f2, start, end):
  
    diff_func = lambda x: abs(f1(x) - f2(x))
    area, error = quad(diff_func, start, end)
    return area