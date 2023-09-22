def myrange(start,stop,step):
    #补充这个生成器函数的代码，实现要求的功能
    #********** Begin *********#
    while start < stop and step >= 0:
        yield start
        start += step
    while start > stop and step < 0:
        yield start
        start += step
    #********** End **********#