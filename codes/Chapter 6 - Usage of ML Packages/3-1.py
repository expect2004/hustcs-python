# -*- coding: utf-8 -*-
import tensorflow as tf

def variables_create():
    '''
    返回值:
    weights: 一个Tensor变量
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    weights = tf.Variable(tf.random_normal([100, 200]), name = "big_weights")
    # ********** End **********#
    # 返回weights

    return weights