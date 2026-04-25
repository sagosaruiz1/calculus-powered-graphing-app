import numpy as np
from scipy.integrate import quad



def get_derivative(f, x_vals, dx=1e-6):

    return (f(x_vals + dx) - f(x_vals)) / dx

def get_integral(f, start, end):

    area, error = quad(f, start, end)
    return area