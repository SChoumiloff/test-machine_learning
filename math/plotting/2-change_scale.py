#!/usr/bin/env python3
"""
24 cm
"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    24 cm
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.plot(x, y)
    plt.yscale('log')
    plt.xlim([x[0], x[-1]])
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")
    plt.show()
