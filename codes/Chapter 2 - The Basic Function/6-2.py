class Solution():

	def solve(self, l, r):
		'''
		:type l, r: int
		:rtype : list
		'''
		#请在此添加代码，实现求得[l, r]范围内的所有素数，并将其返回
		#********** Begin *********#
        def isprime(x):
            if x <= 1:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i = i + 1
            return True
        ret = []
        for i in range(l, r + 1):
            if isprime(i) == True:
                ret.append(i)
        return ret
		#********** End *********#