import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def student(data):
    # ********* Begin *********#
    plt.figure(figsize=(10, 10))
    plt.imshow(data, cmap='hot')
    plt.colorbar()
    plt.savefig('Task1/img/T1.png')
    plt.show()
    # ********* End *********#
