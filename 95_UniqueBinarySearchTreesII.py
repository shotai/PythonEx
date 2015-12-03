# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(start, end):
            if start>end:
                return [None]
            res = []
            for root in range(start, end+1):
                leftlist = helper(start, root-1)
                rightlist = helper(root+1, end)
                for i in leftlist:
                    for j in rightlist:
                        rootnode = TreeNode(root)
                        rootnode.left = i
                        rootnode.right = j
                        res.append(rootnode)
            return res
        if n==0:
            return []
        return helper(1,n)
