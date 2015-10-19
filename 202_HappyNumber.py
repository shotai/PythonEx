class Solution(object):
    def isHappy(self, n):
        import collections
        """
        :type n: int
        :rtype: bool
        """
        while n!=1 and n>4:
            n=sum([int(i)**2 for i in str(n)])
        if n==1:
            return True
        return False
