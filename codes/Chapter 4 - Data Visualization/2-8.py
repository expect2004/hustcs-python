# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import numpy as np
def suoying():
    '''
    返回值:
    d1: 一个DataFrame类型数据
    '''
    #s1是Series类型数据
    s1=Series(np.random.randn(10),
           index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    d1 = s1.unstack()
    # ********** End **********#

    # 返回d1
    return d1





suoying()