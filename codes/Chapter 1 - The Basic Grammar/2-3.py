# coding = utf-8
source_string = input()

# 请在下面添加代码
########## Begin ##########

pos = source_string.find('day')
modify = source_string.replace('day', 'time')
ret = modify.split(' ')

print(pos)
print(modify)
print(ret)

########## End ##########


