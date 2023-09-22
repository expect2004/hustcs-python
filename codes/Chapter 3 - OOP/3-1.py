import specialmethodtest
sc = specialmethodtest.subClass()
# 请在下面填入判断subClass是否为parentClass的子类的代码，并输出结果
########## Begin ##########
print(issubclass(specialmethodtest.subClass, specialmethodtest.parentClass))
########## End ##########
# 请在下面填入判断sc是否为subClass实例的代码，并输出结果
########## Begin ##########
print(isinstance(sc, specialmethodtest.subClass))
########## End ##########
# 请在下面填入判断实例sc是否包含一个属性为name的代码，并输出结果
########## Begin ##########
print(hasattr(sc, 'name'))
########## End ##########
# 请在下面填入将sc的属性name的值设置为subclass的代码
########## Begin ##########
setattr(sc, 'name', 'subclass')
########## End ##########
# 请在下面填入获取sc的属性name的值的代码，并输出结果
########## Begin ##########
print(getattr(sc, 'name'))
########## End ##########
# 请在下面填入调用subClass的父类的tell()方法的代码
########## Begin ##########
super(specialmethodtest.subClass, sc).tell()
########## End ##########