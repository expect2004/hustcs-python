import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def student(input_data,input_data1):
    plt.figure(figsize=(10,10))
    plt.plot(input_data, '--g', label = 'L1')
    plt.plot(input_data1, ':r',label = 'L2')
    plt.legend()
    plt.savefig('Task2/img/T1.png')