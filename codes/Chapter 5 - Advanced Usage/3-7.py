class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #请在此添加代码，实现将二叉树的层次遍历结果返回
        #********** Begin *********#
        Q1 = []
        Q2 = []
        ret = []
        if root == None:
            return ret
        Q1.append(root)
        while True:
            level = []
            for x in Q1:
                if x.left != None:
                    Q2.append(x.left)
                if x.right != None:
                    Q2.append(x.right)
                level.append(x.val)
            ret.append(level)
            if len(Q2) == 0:
                break
            Q1 = Q2
            Q2 = []
        return ret
        #********** End **********#