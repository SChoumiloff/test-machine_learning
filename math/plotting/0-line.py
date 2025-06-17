#!/usr/bin/env python3
"""
plot some shits
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    plot some shits
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, color='red')
    plt.xlim(0, 10)
    plt.show()
