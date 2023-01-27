"""_summary_
Author: ks20447

Created: 27/01/2023

Python file for answering Week 13 Sci Comp python exercises
"""

import numpy as np
import matplotlib.pyplot as plt


def run():
    t = np.linspace(0, 5, 500)
    y = (t**2)*np.exp(-2*t)
    plt.plot(t, y, 'k', linewidth=2)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    idx = np.argmax(y)
    print(t[idx])
    
    
run()