# coding=utf-8

# 输入一个正整数
x = int(input())

# 请在此添加代码，将输入的一个正整数分解质因数
########## Begin ##########

def isprime(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True

result = []
bx = x
for i in range(2, x + 1):
    if isprime(i) == False:
        continue
    while bx > 0 and bx % i == 0:
        result.append(i)
        bx /= i



########## End ##########

# 输出结果，利用map()函数将结果按照规定字符串格式输出
print(x,'=','*'.join(map(str,result)))


