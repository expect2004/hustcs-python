import math
from multiprocessing import cpu_count
from multiprocessing import Pool

N = int(input())
a = list(map(int, input().split()))


def howMany(T):
    ans = 0;
    for i in range(T[0] - 1, T[1]):
        ans = max(ans, a[i])
    return ans
# 对整个数字空间N进行分段CPU_COUNT
def separateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list
    
    
if __name__ == '__main__':
# 多进程
#********** Begin *********#
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



#********** End *********#
