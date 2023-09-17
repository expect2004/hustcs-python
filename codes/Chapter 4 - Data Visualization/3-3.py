import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

def student(x,y,x2,y2,x3,y3,area):
    '''
    根据输入的三组数据绘制三组不同参数的散点图
    :param x,y: 第一组数据，类型为array
    :param x2,y2: 第二组数据，类型为array
    :param x3,y3: 第三组数据，类型为array
    :param area: 标记大小参数的值，类型为array
    :return: None
    '''
    # ********* Begin *********#
    plt.figure(figsize=(10,10))
    plt.scatter(x, y, s=area, alpha=0.5)
    plt.scatter(x2, y2, s=area, c='g', alpha=0.6)
    plt.scatter(x3, y3, s=area, c=area, marker='v', alpha=0.7)
    plt.grid(True)
    plt.savefig('Task3/img/T1.png')
    # ********* End *********#