# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, target):
            if target==node.val and not node.left and not node.right:
                return True
            if node.left and dfs(node.left, target-node.val):
                return True
            if node.right and dfs(node.right, target-node.val):
                return True
            return False
        if not root:
            return False
        return dfs(root, sum)
