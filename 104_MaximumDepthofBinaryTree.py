# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, dep):
            if not root:
                return dep
            return max(dfs(root.left, dep+1), dfs(root.right, dep+1))
        return dfs(root, 0)
