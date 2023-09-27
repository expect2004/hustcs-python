class Stack():
    def __init__(self, size=5):
        self.size = size
        self.stack = []
        self.top = -1
    def is_full(self):
        return self.top+1 == self.size
    def is_empty(self):
        return self.top == -1
    def push(self, x):
        #请在此添加代码，实现将元素x入栈，并在栈满时不进行操作
        #********** Begin *********#
        if self.is_full() == True:
            return
        self.top += 1
        self.stack.append(x)
        #********** End *********#
    def pop(self):
        #请在此添加代码，实现将栈顶元素出栈，并栈顶元素作为返回值返回，栈空时不进行操作
        #********** Begin *********#
        if self.is_empty() == True:
            return None
        ret = self.stack.pop(-1)
        self.top -= 1
        return ret
        #********** End *********#
    def __repr__(self):
        return str(self.stack)