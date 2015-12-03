class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        array = range(1, n+1)
        k = (k%math.factorial(n)) -1
        res = []
        for i in range(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            res.append(array.pop(idx))
        return "".join(map(str, res))
