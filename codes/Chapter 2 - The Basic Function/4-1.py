# coding=utf-8

import math

# 输入正整数a和b
a = float(input())
b = float(input())

# 请在此添加代码，输入直角三角形的两个直角边的边长a和b，计算出其斜边边长
########## Begin ##########


l = a ** 2 + b ** 2
l = math.sqrt(float(l))

print("%.3f" % l)


########## End ##########