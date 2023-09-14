# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import numpy as np
import  pandas as pd

def delete_data():
    '''
    返回值:
    s2: 一个Series类型数据
    d2: 一个DataFrame类型数据
    '''

    # s1是Series类型数据，d1是DataFrame类型数据
    s1 = Series([5, 2, 4, 1], index=['v', 'x', 'y', 'z'])
    d1=DataFrame(np.arange(9).reshape(3,3), columns=['xx','yy','zz'])
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    s2 = s1.drop('z')
    d2 = d1.drop('yy', axis=1)
    # ********** End **********#

    # 返回s2,d2
    return s2, d2




