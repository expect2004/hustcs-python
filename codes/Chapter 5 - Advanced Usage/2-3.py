#coding=utf-8
import math

#输入整数a
a = int(input())

try:
    answer = math.sqrt(a)
# 请在此添加代码，实现编程要求
#********** Begin *********#
except:
    print('We can\'t take a root by minus')
else:
    print(answer)
#********** End **********#