class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(valuelist, start):
            if sum(valuelist)==n and len(valuelist)==k:
                res.append(valuelist)
                return
            if start >9 or len(valuelist)>k:
                return
            for i in range(start, 10):
                helper(valuelist+[i], i+1)
        res = []
        if n>sum([i for i in range(1, 10)]):
            return []
        helper([], 1)
        return res
