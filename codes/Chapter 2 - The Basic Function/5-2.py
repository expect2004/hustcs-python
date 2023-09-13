# coding=utf-8

# 请在此添加代码，使用lambda来创建匿名函数，能够判断输入的两个数值的大小
########## Begin ##########


MAXIMUM = lambda a, b: a if a > b else b
MINIMUM = lambda a, b: a if a < b else b

########## End ##########

# 输入两个正整数
a = int(input())
b = int(input())

# 输出较大的值和较小的值
print('较大的值是：%d' % MAXIMUM(a,b))
print('较小的值是：%d' % MINIMUM(a,b))


