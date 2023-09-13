# 请在下面填入定义Book类的代码
########## Begin ##########
class Book(object):
########## End ##########
    '书籍类'
    def __init__(self,name,author,data,version):
        self.name = name
        self.author = author
        self.data = data
        self.version = version

    def sell(self,bookName,price):
        print("%s的销售价格为%d" %(bookName,price))
    
