class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res
    
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        for i in nums:
            tmp = tmp^i
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        n1, n2 = 0, 0
        for n in nums:
            if n & tmp :
                n1 ^= n
            else:
                n2 ^= n
        return [n1, n2]
