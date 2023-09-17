import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def student(input_data):
    # ********* Begin *********#
    plt.figure(figsize=(10, 10))
    plt.style.use(['classic', 'bmh'])
    plt.hist(input_data, facecolor="red", alpha=0.7)
    plt.savefig("Task4/img/T1.png")
    plt.show()
    # ********* End *********#
