# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            return 1+helper(node.left)
        if not root:
            return 0
        leftd = helper(root.left)
        rightd = helper(root.right)
        if leftd == rightd:
            return pow(2, leftd) + self.countNodes(root.right)
        else:
            return pow(2, rightd) + self.countNodes(root.left)
