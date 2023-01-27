"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

from solvers import *
from scipy import optimize


def func(x):
    f = math.cos(x) - x
    return f


def func_dash(x):
    f_dash = -math.sin(x) - 1
    return f_dash


def run():
    x0 = 0.5
    x1 = 1
    tol = 1e-10
    a = 1
    b = -1
    newt_approx = newton_method(x0, func, func_dash, tol)
    print(newt_approx)
    bisec_approx = bisection_method(func, a, b, tol)
    print(bisec_approx)
    sec_approx = secant_method(func, x0, x1, tol, 1000)
    print(sec_approx)
    sol = optimize.root(func, x0)
    print(sol)
    
    
 
 
run()   