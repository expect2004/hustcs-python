import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif']=['simhei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus']=False

def student(file_path):

    # ********* Begin ********* #
    plt.figure(figsize=(10, 10))
    data = pd.read_csv(file_path)
    a = data["二级类"].groupby(data["二级类"]).count()
    plt.plot(a)
    plt.xticks(rotation=90)  # 旋转90度
    plt.savefig("Task3/img/T1.png")
    plt.show()
    # ********* End *********#
