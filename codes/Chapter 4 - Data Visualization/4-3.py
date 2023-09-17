import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
def student():
    '''
    绘制一个2行4列的不规则子图宽高间隔分别为0.4、0.3。
    第0行设置2个子图，第一个子图占3，第二个子图占1。第二行相反
    :param: None
    :return: None
    '''
    # ********* Begin *********#
    fig = plt.figure(figsize=(10,10))
    grid = plt.GridSpec(2, 4, wspace=0.4, hspace=0.3)
    plt.subplot(grid[0, 0:3])
    plt.subplot(grid[0, -1])
    plt.subplot(grid[-1, 0]) 
    plt.subplot(grid[-1, 1:])
    plt.savefig("Task3/img/T1.png")
    plt.show() 
    # ********* End *********#






