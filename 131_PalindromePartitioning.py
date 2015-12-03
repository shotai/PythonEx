class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def check(st):
            return st == st[::-1]
        def helper(valuelist, st):
            if len(st)==0:
                res.append(valuelist)
                return
            for i in range(1, len(st)+1):
                if check(st[:i]):
                    helper(valuelist+[st[:i]], st[i:])
        if not s:
            return []
        res = []
        helper([], s)
        return res
