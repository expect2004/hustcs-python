import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import matplotlib as mpl
def student(file_name):
    # ********* Begin *********#
    fig = plt.figure(figsize=(10,10))
    data = pd.read_csv(file_name)
    #去空置处理
    #data = data.dropna(axis=0,subset = ["year", "births"])
    data = data.dropna(axis=0,how='any')  #本题要求全部都不为空
    data = data.groupby(['year'])[['births']].sum()
    plt.plot(data.index,data.values)
    #dic = data.set_index("year")['births'].to_dict()
    dic = data.to_dict()
    dic = dic['births']
    maxx=max(dic,key=dic.get)
    minn=min(dic,key=dic.get)
    #plt.annotate('max', xy=(maxx,dic[maxx]), xytext=(maxx-5,dic[maxx]-5))#注释仅为文本，（‘注释内容’，注释的点的坐标，注释文本的坐标）
    plt.annotate('max', xy=(maxx,dic[maxx]), xytext=(maxx-5,dic[maxx]-5), arrowprops=dict(facecolor='black', shrink=0.05))#注释为箭头+文本，（‘注释内容’，注释的点的坐标，注释文本的坐标，箭头设置）
    plt.annotate('min', xy=(minn,dic[minn]), xytext=(minn-5,dic[minn]-5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.savefig('Task2/img2/T5.png')
    # ********* End *********#