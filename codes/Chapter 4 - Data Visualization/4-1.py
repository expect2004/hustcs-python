import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

def student(x):
    '''
    根据输入数据绘制不同的两个子图
    :param x: 输入数据，类型为array
    :return: None
    '''
    # ********* Begin *********#
    fig=plt.figure(figsize=(12,12))
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    ax1.plot(x,x**2,ls='--',c="red",lw=1,alpha=0.3)
    ax2.plot(x,np.log(x))
    plt.savefig('Task1/img/T1.png')
    plt.show()
    # ********* End *********#