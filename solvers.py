"""_summary_
Author: ks20447

Created: 27/01/2023

Python Module to run numerical solvers
"""

import math
import numpy as np


def newton_method(x0, f, f_dash, tol):
    error = math.inf
    x_n = x0
    while error > tol:
        x_new = x_n - (f(x_n)/f_dash(x_n))
        x_n = x_new
        error = abs(f(x_n))
    return x_n


def bisection_method(f, a, b, tol): 
    if np.sign(f(a)) == np.sign(f(b)):
        print("The scalars a and b do not bound a root")
        return 0 
    
    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection_method(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection_method(f, a, m, tol)
    


def secant_method(f, x0, x1 , e, N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    return x2
    
        
