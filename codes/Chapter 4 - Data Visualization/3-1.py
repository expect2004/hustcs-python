import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def student(x,y):
    # ********** Begin *********#
    plt.figure(figsize=(10,10))
    # plt.subplot(1, 1, 1)
    plt.plot(x, y)
    plt.savefig("Task1/image1/T2.png")
    # ********** End **********#