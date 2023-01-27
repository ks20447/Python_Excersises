"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np


def solve(a_mat, b):
    x = np.linalg.solve(a_mat, b)
    result = np.matmul(a_mat, x) - b
    print(x)
    print(result)


def run():
    a_mat = np.array([[1, 0, 0, 0], [1, -2, 1, 0], [0, 1, -2, 1], [0, 0, 0, 1]])
    b = np.array([[0], [1], [1], [2]])
    solve(a_mat, b)
    
    
run()