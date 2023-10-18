import math
from multiprocessing import cpu_count
from multiprocessing import Pool

# 判断数字是否为质数
#********** Begin *********#
# def isPrime(n):
#     if n==1:
#         return False
#     elif n==2:
#         pass
#     else:
#         for i in range(2,n//2+1):
#             if (n%i==0):
#                 return False
#     return True
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


#********** End *********#

# 计算给定区间含有多少个质数
#********** Begin *********#
# def howMany(T):
#     cnt=0
#     for i in range(T[0],T[1]):
#         if isPrime(i):
#             cnt+=1
#     return cnt



# #********** End *********#

# # 对整个数字空间N进行分段CPU_COUNT
# #********** Begin *********#
# def separateNum(N, CPU_COUNT):

#     l=[]
#     n=N//(CPU_COUNT-1)

#     for i in range(CPU_COUNT-1):
#         l.append((i*n+1,(i+1)*n+1))

#     l.append(((i+1)*n+1,N+1))
#     return l
def howMany(T):
    sum = 0;
    for i in range(T[0], T[1] + 1):
        if isPrime(i):
            sum += 1
    return sum

# 对整个数字空间N进行 分段CPU_COUNT
def separateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list
    



#********** End *********#

if __name__ == '__main__':
    N = int(input())
    # 多进程
    CPU_COUNT = cpu_count()  ##CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = separateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(howMany, (sepList[i], )))
    pool.close()
    pool.join()
    ans = 0
    list = [res.get() for res in result]
    print(sum(list), end = '')
