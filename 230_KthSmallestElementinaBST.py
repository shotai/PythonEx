# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return
            for v in dfs(node.left):
                yield v
            yield node.val
            for v in dfs(node.right):
                yield v
        return next(itertools.islice(dfs(root), k-1, k))
