"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np


def vector_calc(a, b):
    if len(a) == len(b):
        ab_dot = np.dot(a, b)
        print(f"{ab_dot}")
    else:
        print(f"Vectors are inconsitent")
  
  
def matrix_calc(a_mat):
    if len(a_mat[0]) == len(a_mat[1]): 
        a_mat_prod = np.prod(a_mat)
        print(f"{a_mat_prod}")
    else:
        print(f"Matrix is inconsistent")


def run():
    a = np.array([1, 2, 3, 4])
    b = np. array([6, 5, 4])
    vector_calc(a, b)
    
    a_mat = [[1, 2], [3, 4, 5]]
    matrix_calc(a_mat)
    
    
run()