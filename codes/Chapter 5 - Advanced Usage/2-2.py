#coding=utf-8

#输入字符串
s = input()

# 请在此添加代码，将字符串s输入到test2.txt中
#********** Begin *********#
with open('src/Step2/test2.txt', 'w') as oup:
   oup.write(s) 
#********** End **********#

#输出test2.txt中的内容
with open('src/Step2/test2.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

