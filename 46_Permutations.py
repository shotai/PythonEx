class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start, end, nums):
            if(start == end-1):
                res.append(list(nums))
            for k in range(start, end):
                nums[start], nums[k] = nums[k], nums[start]
                helper(start+1, end, nums)
                nums[start], nums[k] = nums[k], nums[start]
        
        res = []
        helper(0, len(nums), nums)
        return res
        
    def permute_iter(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not num:
            return []
        ret = [[]]
        for n in num:
            tmp_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    tmp_ret.append(seq[:i] + [n] + seq[i:])
            ret = tmp_ret
        return ret
