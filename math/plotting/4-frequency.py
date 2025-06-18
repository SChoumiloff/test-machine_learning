#!/usr/bin/env python3
"""
Lost frequencies
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Lost frequencies
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.hist(
        student_grades,
        bins=[10*x for x in range(0, 11)],
        edgecolor='black'
    )
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks([x for x in range(0, 101, 10)])
    plt.title("Project A")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()
