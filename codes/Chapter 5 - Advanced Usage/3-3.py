class Queue():
    def __init__(self, size=5):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = []
    def is_full(self):
        return self.rear - self.front == self.size
    def is_empty(self):
        return self.front == self.rear
    def en_queue(self, x):
        #请在此添加代码，实现将元素x入队，并在队满时不进行操作
        #********** Begin *********#
        if self.is_full() == True:
            return
        self.rear += 1
        self.queue.append(x)
        #********** End *********#
        
    def de_queue(self):
        #请在此添加代码，实现将队首元素出队，并在队空时不进行操作
        #********** Begin *********#
        if self.is_empty() == True:
            return
        self.front += 1
        self.queue.pop(0)
        #********** End *********#
        
    def __repr__(self):
        return str(self.queue)