# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def create_dataframe():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    dict = {'states':[1,2,3,4,5], 'years':[6,7,8,9,10],'pops':[11,12,13,14,15]}
    frame = DataFrame(dict, index = ['one', 'two', 'three', 'four', 'five'])
    frame['new_add'] = [7, 4, 5, 8, 2]
    df1 = frame
    # ********** End **********#

    #返回df1
    return df1