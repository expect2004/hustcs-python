import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

def student():
    '''
    绘制不同一个两行四列的网格子图，并设置图形高度与宽度为0.4
    :param: None
    :return: None
    '''
    # ********* Begin *********#
    fig = plt.figure(figsize=(10,10))
    fig.subplots_adjust(hspace=0.4,wspace=0.4)
    for i in range(1,9):
        plt.subplot(2,4,i)
    plt.savefig("Task2/img/T1.png")

    plt.show()

    # ********* End *********#


