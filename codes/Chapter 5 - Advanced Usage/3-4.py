class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #请在此添加代码，实现判断字符串s是否合法，若合法，返回True，否则返回False
        #********** Begin *********#
        stack = []
        l = len(s)
        for i in range(0, l):
            ch = s[i]
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                tp = stack.pop()
                if (ch == ']' and tp != '[') or (ch == '}' and tp != '{') or (ch == ')' and tp != '('):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        #********** End **********#