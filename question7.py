"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np


def pseudoinverse(a):
    a_t = np.transpose(a)
    a_inv = np.matmul(a_t, a)
    a_inv = np.linalg.inv(a_inv)
    a_inv = np.matmul(a_inv, a_t)
    return a_inv
    
    
def run():
    a = np.array([[1, -1], [2, 4], [1, 1], [3, 8]])
    a_inv = pseudoinverse(a)
    print(np.matmul(a_inv, a))
    b = np.array([[2], [4], [6], [8]])
    x = np.matmul(a_inv, b)
    print(x)
  
    
run()