# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def dfs(node):
            if not node:
                return
            for i in dfs(node.left):
                yield i
            yield node.val
            for j in dfs(node.right):
                yield j
        
        self.res = dfs(root)
        self.nextone = next(self.res,None)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nextone==None:
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        tmp = self.nextone
        self.nextone = next(self.res,None)
        return tmp

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
