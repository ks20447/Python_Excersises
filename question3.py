"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np


def run():
    a = np.array([5, 4, 9, 2, 0, 4, 7, 2 ,-9])
    print(f"Last entry: {a[-1]}")
    print(f"Entries 1 through 6: {a[1:6]}")
    print(f"All entries up to second to last: {a[:-2]}")
    print(f"Every other entry from first: {a[::2]}")
    a[0:3] = 1
    print(f"{a}")


run()