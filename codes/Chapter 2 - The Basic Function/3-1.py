changeOne = int(input())
changeTwo = int(input())
plus = int(input())

# 请在此添加代码，交换changeOne、changeTwo的值，然后计算changeOne、plus的和result的值
########## Begin ##########


tmp = changeOne
changeOne = changeTwo
changeTwo = tmp

result = plus + changeOne


########## End ##########
print(result)
