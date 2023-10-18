import threading
import math
ans = 0
lock = threading.Lock()
# 判断数字是否为质数
#********** Begin *********#
def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True



#********** End *********#


#********** Begin *********#
# 计算给定区间含有多少个质数
def howMany(T):
    lock.acquire()
    global ans
    for i in range(T[0], T[1] + 1):
        if isPrime(i):
            ans += 1
    lock.release()

# 对整个数字空间N进行 分段CPU_COUNT
def seprateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list

lock=threading.Lock()
ans=0

#********** End *********#


if __name__ == '__main__':
    N = int(input())
    threadNum = 32
    t = []
    sepList = seprateNum(N, threadNum)
    for i in range(0, threadNum):
        t.append(threading.Thread(target = howMany, args = (sepList[i], )))
        t[i].start()
    for i in range(0, threadNum):
        t[i].join()
    print(N - 1 - ans, end = '')