#有错误的函数1
def wrong1():
    print("wrong1")
    print("这里有一个错误缩进")
	
#有错误的函数2
def wrong2():
    print("wrong2")
    if False:
        print("这个不应该输出")
        print("这个也不应该输出")

#有错误的函数3
def wrong3():
    print("wrong3")
    print("hello world")


#这里是调用三个函数的代码
#不要修改
if __name__ == '__main__':

    wrong1()
    wrong2()
    wrong3()