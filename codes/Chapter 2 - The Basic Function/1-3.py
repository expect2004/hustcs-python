# coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最小公倍数
########## Begin ##########
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)



########## End ##########

# 调用函数，并输出a,b的最小公倍数
print(lcm(a,b))

