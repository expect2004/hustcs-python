# -*- coding:utf-8 -*-

def learn(train_data, N, M):
	"""从训练数据中学习得到模型
	参数:
		train_data - Pandas的DataFrame对象，有四列'user','movie','rating','timestamp'，是训练数据集
		N - 整数，用户数目
		M - 整数，电影数目		
	返回值：
		g - 数据集中的平均每用户每电影评分值参数
		alpha - 浮点数组，用户评分偏差参数数组，举例alpha[9]表示用户9的评分偏差
		beta - 浮点数组，电影评分偏差参数数组，举例beta[90]表示电影90的评分偏差
	"""		
	#导入Step2的模块
	from stat_rating import avg_rating_of_users_movies
	import numpy as np	
	
	#模型参数
	g = 0#模型参数：所有用户所有电影的平均评分
	alpha = np.zeros(N)#模型参数：每个用户的评分偏好
	beta = np.zeros(M)#模型参数：每个电影的评分偏好
	
	# 请在此添加实现代码
	#********** Begin *********#		
	g = train_data['rating'].mean()
    for i in range(0, N):
        alpha[i] = -g
    for i in range(0, M):
        beta[i] = -g
    U = train_data.groupby('user').agg({'rating':np.mean})
    for index, row in U.iterrows():
        alpha[index] = row['rating'] - g
    M = train_data.groupby('movie').agg({'rating':np.mean})
    for index, row in M.iterrows():
        beta[index] = row['rating'] - g
	#**********  End  *********#
	
	return g, alpha, beta