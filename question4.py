"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np


def random_array(n , lower, upper):
    rand_array = np.random.randint(lower, upper, n)
    return rand_array


def run():
    r = random_array(20, 1, 9)
    print(r)
    idx = r < 5
    print(idx)
    r[idx] = 0
    print(r)
    
    
run()