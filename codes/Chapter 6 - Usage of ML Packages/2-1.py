# -*- coding:utf-8 -*-

def stat_data(train_data):
    """求出用户数和电影数，评分数目, 平均评分, 最大评分, 最小评分
    参数:
        train_data - Pandas的DataFrame对象，有四列'user','movie','rating','timestamp'，是训练数据集
    返回值：
        num_user - 整数，用户数
        num_movie - 整数，电影数
        num_rating - 整数，评分数目
        avg_rating - 浮点数，平均评分
        max_rating - 浮点数，最大评分
        min_rating - 浮点数，最小评分
    """
    num_user = 0
    num_movie = 0
    num_rating = 0
    avg_rating = 0
    max_rating = 0
    min_rating = 0
    # 请在此添加实现代码
    #********** Begin *********#        
    num_user = len(train_data['user'].unique())
    num_movie = len(train_data['movie'].unique())
    num_rating = train_data['rating'].size
    avg_rating = train_data['rating'].mean()
    max_rating = train_data['rating'].max()
    min_rating = train_data['rating'].min()
    #**********  End  *********#
    return num_user, num_movie, num_rating, avg_rating, max_rating, min_rating 
    