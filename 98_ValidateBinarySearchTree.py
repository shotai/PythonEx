# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, mi, ma):
            if not node:
                return True
            if node.val>=ma:
                return False
            if node.val<=mi:
                return False
            return dfs(node.left, mi, node.val) and dfs(node.right,node.val,ma)
            
        if not root:
            return True
        return dfs(root, float("-infinity"), float("infinity"))
        
