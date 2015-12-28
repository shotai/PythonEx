class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <2:
            return nums
        
        ret = nums[:]
        for i in range(1, len(nums)-1):
            ret[i] *= ret[i-1]
        
        rt = 1
        for i in range(len(nums)-1, 0, -1):
            ret[i] = ret[i-1]*rt
            rt *= nums[i]
        ret[0] = rt
        return ret
