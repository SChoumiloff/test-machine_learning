#!/usr/bin/env python3
"""
One man one jar
"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
    One man one jar
    """
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)

    # Create a multi-figure plot
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Plot y0
    axs[0, 0].plot(np.arange(0, 11), y0, 'r-')
    axs[0, 0].set_title("y = x^3")
    axs[0, 0].set_xlabel("x")
    axs[0, 0].set_ylabel("y")

    # Plot x1, y1
    axs[0, 1].scatter(x1, y1, c='purple', alpha=0.5)
    axs[0, 1].set_title("Multivariate Normal Distribution")
    axs[0, 1].set_xlabel("x")
    axs[0, 1].set_ylabel("y")

    # Plot x2, y2
    axs[0, 2].plot(x2, y2, 'g-')
    axs[0, 2].set_title("Exponential Decay (Half-life)")
    axs[0, 2].set_xlabel("Time")
    axs[0, 2].set_ylabel("y")

    # Plot x3, y31
    axs[1, 0].plot(x3, y31, 'b-', label="Half-life = 5730")
    axs[1, 0].plot(x3, y32, 'orange', label="Half-life = 1600")
    axs[1, 0].set_title("Exponential Decay Comparison")
    axs[1, 0].set_xlabel("Time")
    axs[1, 0].set_ylabel("y")
    axs[1, 0].legend()

    # Plot student grades histogram
    axs[1, 1].hist(student_grades, bins=10, color='cyan', edgecolor='black')
    axs[1, 1].set_title("Student Grades Distribution")
    axs[1, 1].set_xlabel("Grades")
    axs[1, 1].set_ylabel("Frequency")

    # Remove unused subplot
    axs[1, 2].axis('off')

    # Adjust layout
    plt.tight_layout()
    plt.show()
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # your code here
all_in_one()