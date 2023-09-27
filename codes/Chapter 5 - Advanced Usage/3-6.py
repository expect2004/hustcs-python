class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #请在此添加代码，实现将二叉树的后序遍历结果返回
        #********** Begin *********#
        stack = []
        ret = []
        if root == None:
            return ret
        stack.append(root)
        while len(stack) > 0:
            x = stack[-1]
            if x.left != None:
                stack.append(x.left)
                x.left = None
                continue
            if x.right != None:
                stack.append(x.right)
                x.right = None
                continue
            ret.append(x.val)
            del stack[-1]
        return ret
        #********** End **********#