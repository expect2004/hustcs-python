import re
text = input()
#********** Begin *********#
#1.用compile方法，匹配所有含字母i的单词
rr = re.compile(r'\b\w*i\w*\b')
print(rr.findall(text))

#2.在字符串起始位置匹配字符The是否存在，并返回被正则匹配的字符串
print(re.match('The',text).group())

#3.在整个字符串查看字符is是否存在，并返回被正则匹配的字符串
print(re.search('is',text).group())

#********** End **********#