# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(start, end):
            if start>end:
                return None
            mid = (start+end)/2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid-1)
            node.right = helper(mid+1, end)
            return node
        if nums is None:
            return None
        return helper(0, len(nums)-1)
