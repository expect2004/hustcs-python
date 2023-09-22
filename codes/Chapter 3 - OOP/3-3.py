class WrapClass(object):
    def __init__(self,obj):
        self.__obj = obj
    def get(self):
        return self.__obj
    def __repr__(self):
        return 'self.__obj'
    def __str__(self):
        return str(self.__obj)
    # 请在下面填入重写__getattr__()实现授权的代码
    ########## Begin ##########
    def __getattr__(self,thelist):
        if thelist == 'thelist':
            return self.__obj

    ########## End ##########


thelist = []
inputlist = input()
for i in inputlist.split(','):
    result = i
    thelist.append(result)
# 请在下面填入实例化类，并通过对象调用thelist，并输出thelist第三个元素的代码
########## Begin ##########
test = WrapClass(thelist)
print(test.thelist[2])



########## End ##########

