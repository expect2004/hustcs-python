import re
text = input()
#********** Begin *********#
#1.匹配以t开头的所有单词并显示
itext = re.finditer(r'\bt\w*\b', text)
for i in itext:
    print(i.group())
#2.用空格分割句子
print(re.split(r' ', text))
#3.用‘-’代替句子中的空格 
print(re.sub(r' ', '-', text))
#4.用‘-’代替句子中的空格，并返回替换次数
print(re.subn(r' ', '-', text))
#********** End **********#