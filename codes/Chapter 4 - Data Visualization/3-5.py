import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def student(labels, quants):
    plt.figure(figsize=(6,6))
    plt.pie(quants,labels=labels,explode=(0,0.1,0,0,0,0,0,0,0,0),autopct='%1.1f%%')
    plt.savefig('Task5/img/T1.png')