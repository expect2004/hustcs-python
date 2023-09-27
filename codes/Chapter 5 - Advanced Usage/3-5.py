class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #请在此添加代码，实现将含有逆波兰表达式的list转换成其对应表达式的值，并返回
        #********** Begin *********#
        stack = []
        oplist = ['+', '-', '*', '/']
        for ch in tokens:
            if ch not in oplist:
                stack.append(int(ch))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                val = 0
                if ch == '+':
                    val = val1 + val2
                elif ch == '-':
                    val = val1 - val2
                elif ch == '*':
                    val = val1 * val2
                else:
                    kval = 1 if val1 * val2 >= 0 else -1
                    val = abs(val1) // abs(val2) * kval 
                stack.append(val)
        return stack[0]
        #********** End **********#