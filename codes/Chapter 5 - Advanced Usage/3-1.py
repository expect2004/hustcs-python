ls = list(map(lambda x:int(x), input().split(',')))

#请在此添加代码，实现将修改后的list、队首元素和队尾元素输出
#********** Begin *********#
ls.extend([4, 5, 6])
ls.append([7, 8, 9])
print(ls)
print(ls[0])
print(ls[-1])
#********** End **********#