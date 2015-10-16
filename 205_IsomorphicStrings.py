class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = t[i]
        tmp = []
        for i in range(len(s)):
            tmp.append(dict[s[i]])
        if ''.join(tmp) != t:
            return False
        for i in range(len(t)):
            dict[t[i]]=s[i]
        tmp = []
        for i in range(len(t)):
            tmp.append(dict[t[i]])
        if ''.join(tmp)!=s:
            return False
        return True
