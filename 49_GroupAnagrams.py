class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        dict = {}
        res = []
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp in dict:
                dict[tmp].append(i)
            else:
                dict[tmp] = [i]
        for item in dict:
            dict[item].sort()
            res.append(dict[item])
        return res
    
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        res = []
        strs.sort()
        dic = collections.defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            dic[k].append(s)
        for k, v in dic.items():
            res.append(v)
        return res
