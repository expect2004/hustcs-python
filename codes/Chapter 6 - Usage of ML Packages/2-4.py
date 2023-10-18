# -*- coding:utf-8 -*-

def predict(g, alpha, beta, test_data):
    """预测用户对电影的评分
    参数:
        g - 浮点数，模型参数平均电影评分参数
        alpha - 浮点数组，用户评分偏差参数数组
        beta - 浮点数组，电影评分偏差参数数组
        test_data - Pandas的DataFrame对象，有两列'user','movie'，是测试数据集
    返回值：
        ret - 浮点数数组，预测的评分数组，每个值对应test_data中的每一行的评分值
    """
    ret = []
    N = len(alpha)
    M = len(beta)
    
    # 请在此添加实现代码
    #********** Begin *********#        
    for index, data in test_data.iterrows():
        ret.append(g + alpha[data['user']] + beta[data['movie']])
    #**********  End  *********#
    
    return ret