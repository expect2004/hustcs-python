# -*- coding:utf-8 -*-

def gradient(u, m, r, g, alpha, beta):
	"""求出用户权重的梯度
	参数:
		u - 整数，用户ID
		m - 整数，电影ID
		r - 整数，实际评分
		g - 浮点数，平均评分参数
		alpha - 浮点数组，用户评分偏差参数数组
		beta - 浮点数组，电影评分偏差参数数组
	返回值：
		grad_alpha - 浮点数，用户梯度值，举例grad_alpha[9]表示用户9的评分偏差梯度
		grad_beta - 浮点数，电影梯度值，举例grad_beta[90]表示电影90的评分偏差梯度
	"""
	grad_alpha = 0
	grad_beta = 0
	# 请在此添加实现代码
	#********** Begin *********#		
	e = r - g - alpha[u] - beta[m]
    grad_alpha = -2 * e
    grad_beta = -2 * e
	#**********  End  *********#
	
	return grad_alpha, grad_beta
	
def learn(train_data, N, M, steps, tao, g):
	"""学习模型
	参数:
		train_data - Pandas的DataFrame对象，有四列'user','movie','rating','timestamp'，是训练数据集		
		N - 整数，用户数目
		M - 整数，电影数目
		steps - 整数，迭代次数
		tao - 浮点数，学习速率
		g - 浮点数，平均电影评分
	返回值：
		alpha - 浮点数组，用户评分偏差参数数组，举例alpha[9]表示用户9的评分偏差
		beta - 浮点数组，电影评分偏差参数数组，举例beta[90]表示电影90的评分偏差
	"""
	import numpy as np

	#以正态分布初始化模型参数bu和bi
	alpha = np.zeros(N)+0.01
	beta = np.zeros(M)+0.01
	
	#迭代循环
	for step in range(steps):
		for row in train_data.itertuples():
			u = row.user
			m = row.movie
			r = row.rating
			# 请在此添加实现代码
			#********** Begin *********#		
	        ga, gb = gradient(u, m, r, g, alpha, beta)
            alpha[u] = alpha[u] - ga * tao
            beta[m] = beta[m] - gb * tao
			#**********  End  *********#
			
	return alpha, beta