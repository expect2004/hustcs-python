# 引入numpy库
import numpy as np
# 定义varray函数
def  vsarray(m,n):
    '''
    参数：
    m：是第一个数组
    n：是需要拆分到的维度
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0
    # 请在此添加代码实现数组的纵向拆分并赋值给ret
    #********** Begin *********#
    ret = np.vsplit(m, n)
    #********** End **********#
    return ret
# 定义darray函数
def  dsarray(m,n):
    '''
    参数：
    m：是第一个数组
    n：是需要拆分到的维度
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0
    # 请在此添加代码实现数组的深度拆分并赋值给ret
    #********** Begin *********#
    ret = np.dsplit(m, n)
    #********** End **********#
    return ret
 # 定义harray函数
def  hsarray(m,n):
    '''
    参数：
    m：是第一个数组
    n：是需要拆分到的维度
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0
    # 请在此添加代码实现数组的水平拆分并赋值给ret
    #********** Begin *********#
    ret = np.hsplit(m, n)
    #********** End **********#
    return ret