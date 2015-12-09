class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr = res = nums[0]
        for n in nums[1:]:
            curr = max(n, curr+n)
            res = max(res, curr)
        return res
