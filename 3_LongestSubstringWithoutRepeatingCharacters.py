class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1
        for i, v in enumerate(s):
            if dict[v] != -1:
                start = dict[v]+1 if start<=dict[v] else start
            if maxlen < i-start+1:
                maxlen = i-start+1
            dict[v] = i
        return maxlen
