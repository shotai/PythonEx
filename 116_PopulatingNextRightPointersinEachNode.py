# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def dfs(nextlevel):
            if not nextlevel:
                return
            tmp = []
            curr = nextlevel[0]
            if curr.left:
                tmp.append(curr.left)
            if curr.right:
                tmp.append(curr.right)
            for i in nextlevel[1:]:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
                curr.next = i
                curr = curr.next
            dfs(tmp)
        if not root:
            return
        dfs([root])
