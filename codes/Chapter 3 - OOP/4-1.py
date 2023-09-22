class FibIterator:
    count = 0
    now = 1 #初始值分别设置为1和0，方便__next__函数处理
    last = 0 #
    def __init__(self,count):
        self.count = count
    def __iter__(self):
        return self
    def __next__(self):
        #********** Begin *********#
        if self.count:
            t = self.now
            self.now = t + self.last
            self.last = t
            self.count -= 1
            return t
        else:
            raise StopIteration
        #********** End **********#
def GetFib(count):
    return FibIterator(count)


