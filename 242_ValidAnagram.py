class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a1 = dict()
        a2 = dict()
        l = len(s)
        if l!=len(t):
          return False
        for i in range(l):
            a1[s[i]] = a1.get(s[i], 0) + 1
            a2[t[i]] = a2.get(t[i], 0) + 1
        return a1==a2
