class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k ==0:
            return[[]]
        res = []
        for i in range(1, n+1):
            for pre in self.combine(i-1, k-1):
                res.append(pre+[i])
        return res
