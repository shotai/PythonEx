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
