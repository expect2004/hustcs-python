# coding=utf-8

# 导入math模块
import math

# 输入两个整数a和b
a = int(input())
b = int(input())

# 请在此添加代码，要求判断是否存在两个整数，它们的和为a，积为b
########## Begin ##########

Flag = False

for i in range(1, a - 1):
    la = i
    lb = a - i
    if la * lb == b:
        Flag = True
        break

if Flag:
    print('Yes')
else:
    print('No')


########## End ##########