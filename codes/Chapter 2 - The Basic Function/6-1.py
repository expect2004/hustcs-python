class Solution():

    
	def get_lcm(self, x):
		'''
		:type x: list
		:rtype : int
		'''
		#请在此添加代码，实现求出给定的所有正整数的最小公倍数，并将其返回
		#********** Begin *********#
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        ret = 1
        for num in x:
            ret = ret * num // gcd(ret, num)
        return ret
		##********** End **********#
        pass