# -*- coding:utf-8 -*-
import math
def RMSE(predicted_rating, true_rating):
	"""计算RMSE值
	参数:
		predicted_rating - list，预测的评分
		true_rating - list，真实的评分
	返回值：
		rmse - 浮点数，RMSE值
	"""
	rmse = 0
	# 请在此添加实现代码
	#********** Begin *********#		
	for i in range(0, len(predicted_rating)):
        rmse += (predicted_rating[i] - true_rating[i]) ** 2
    rmse /= len(predicted_rating)
    rmse = math.sqrt(rmse)
	#**********  End  *********#
	
	return rmse