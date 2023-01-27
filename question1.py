"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import math


def leibniz_approximation(n):
    pi_approx = 0
    for i in range(n):
        pi_approx += 8/((4*i + 1)*(4*i + 3))
    error = abs(math.pi - pi_approx)
    return pi_approx, error


def run():
    N1, N2, N3 = 100, 1000, 10000
    print(f"Pi approximation for N = {N1}: pi = {leibniz_approximation(N1)[0]}, error = {leibniz_approximation(N1)[1]}")
    print(f"Pi approximation for N = {N2}: pi = {leibniz_approximation(N2)[0]}, error = {leibniz_approximation(N2)[1]}")
    print(f"Pi approximation for N = {N3}: pi = {leibniz_approximation(N3)[0]}, error = {leibniz_approximation(N3)[1]}")
    N = 1000000
    error, tolerance = math.inf, 10**(-7) 
    while error > tolerance:
        error = leibniz_approximation(N)[1]
        N += 1000000
    print(f"N required for error < 10^(-7): {N}")

run()
