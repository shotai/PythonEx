class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        li = [len(i) for i in strs]
        m = min(li)
        res = []
        init = strs[0]
        tmp=True
        for i in range(m):
            for s in range(1,len(strs)):
                 if strs[s][i] != init[i]:
                     tmp = False
                     break
            if tmp:
                res.append(init[i])
            else:
                break
        return ''.join(res)
