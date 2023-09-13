import fractionSumtest
# 请在下面填入创建fractionSum的实例fs的代码
########## Begin ##########
fs = fractionSumtest.fractionSum()
########## End ##########
n = int(input())
if n % 2 == 0:
    # 请在下面填入调用fractionSumtest类中dcall方法的代码，计算当n为偶数时计算的和
    ########## Begin ##########
    sum = fs.dcall(fs.peven, n)
    ########## End ##########
else:
    # 请在下面填入调用fractionSumtest类中dcall方法的代码，计算当n为奇数时计算的和
    ########## Begin ##########
    sum = fs.dcall(fs.podd, n)
    ########## End ##########
print(sum)