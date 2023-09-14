# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
def sort_gate():
    '''
    返回值:
    s2: 一个Series类型数据
    d2: 一个DataFrame类型数据
    '''

    # s1是Series类型数据，d1是DataFrame类型数据
    s1 = Series([4, 3, 7, 2, 8], index=['z', 'y', 'j', 'i', 'e'])
    d1 = DataFrame({'e': [4, 2, 6, 1], 'f': [0, 5, 4, 2]})

    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    s2 = s1.sort_index()
    d2 = d1.sort_values(by = 'f')
    # ********** End **********#



    #返回s2,d2
    return s2,d2




