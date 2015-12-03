class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        minv = maxv = res = nums[0]
        for i in range(1, len(nums)):
            a = minv*nums[i]
            b = maxv*nums[i]
            c = nums[i]
            minv = min(a,b,c)
            maxv = max(a,b,c)
            res = maxv if maxv>res else res
        return res
