class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        cache = {"":True}
        def dfs(substr):
            if substr in cache:
                return cache[substr]
            for i in range(len(substr)):
                if (substr[:i+1] in wordDict) and dfs(substr[i+1:]):
                    cache[substr] = True
                    return True
            cache[substr]=False
            return False
        return dfs(s)
