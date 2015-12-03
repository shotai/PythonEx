# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def binarysearch(start, end):
            if start>end:
                return
            mid = (start+end)/2
            node = TreeNode(num[mid])
            node.left = binarysearch(start, mid-1)
            node.right = binarysearch(mid+1, end)
            return node
        
        num = []
        curr = head
        while curr:
            num.append(curr.val)
            curr = curr.next
        return binarysearch(0, len(num)-1)
