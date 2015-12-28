class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(l, r, valuelist):
            if r<l:
                return
            if r==0 and l==0:
                res.append(valuelist)
            if r>0:
                dfs(l, r-1, valuelist+')')
            if l>0:
                dfs(l-1,r,valuelist+'(')
        if n==0:
            return []
        res = []
        dfs(n,n,'')
        return res
