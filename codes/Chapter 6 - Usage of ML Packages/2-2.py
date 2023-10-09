# -*- coding:utf-8 -*-
import numpy
def avg_rating_of_users_movies(data):
	"""求出每个用户的平均评分
	参数:
		data - Pandas的DataFrame对象，有四列'user','movie','rating','timestamp'，是训练数据集
	返回值：
		user2avg_r - Pandas的DataFrame对象，有一列'rating'
		movie2avg_r - Pandas的DataFrame对象，有一列'rating'
	"""
	user2avg_r = ''
	movie2avg_r = ''
	# 请在此添加实现代码
	#********** Begin *********#		
	user2avg_r = data.groupby('user').agg({'rating' : numpy.mean})
    movie2avg_r = data.groupby('movie').agg({'rating' : numpy.mean})
	#**********  End  *********#	
	return user2avg_r, movie2avg_r
	
def top_10_user_movie_on_avg_rating(user2avg_r, movie2avg_r):	
	"""求出平均评分最高的10个用户和10个电影
	参数:
		user2avg_r - Pandas的DataFrame对象，有一列'rating'
		movie2avg_r - Pandas的DataFrame对象，有一列'rating'
	返回值：
		top10_users - 整数列表，用户ID数组，比如[3,4,5,6]代表前4个用户账户是3,4,5,6
		top10_movies - 整数列表，电影ID数组，比如[30,40,50,60]代表前4个电影编号是3,4,5,6
	"""
	top10_users = []
	top10_movies = []
	# 请在此添加实现代码
	#********** Begin *********#		
    top10_users = list(((user2avg_r.sort_values(by='rating',ascending=False))[:10]).index)
    top10_movies = list(((movie2avg_r.sort_values(by='rating',ascending=False))[:10]).index)
	#**********  End  *********#
	return top10_users, top10_movies