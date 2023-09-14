# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
def read_csv_data():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    length1: 一个int类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    df1 = pd.read_csv('test3/uk_rain_2014.csv', header = 0)
    df1.columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
    length1 = len(df1)
    # ********** End **********#
    #返回df1,length1
    return df1,length1
