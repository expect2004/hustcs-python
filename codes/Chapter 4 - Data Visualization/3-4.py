import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt


def student(data, x, y):
    '''
    根据输入数据将直方图与线形图绘制在同一面板中，并设置直方图为红色，线形图为蓝色
    :param data: 绘制直方图数据，类型为list
    :param x,y: 绘制线形图数据，类型为list

    :return: None
    '''
    # ********* Begin *********#
    plt.figure(figsize=(10,10))
    plt.hist(data,facecolor='red')
    plt.plot(x,y,color='b')
    plt.savefig('Task4/img/T1.png')
    # ********* End *********#