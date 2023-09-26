#coding=utf-8

#输入n
n = int(input())

with open('src/Step1/test.txt') as file_object:
    lines = file_object.readlines()

# 请在此添加代码，实现编程要求
#********** Begin *********#
for i in range(0, n):
    print(lines[i].rstrip())
#********** End **********#