class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mi = ma = res = nums[0]
        for i in nums[1:]:
            a = mi*i
            b = ma*i
            mi = min(a, b, i)
            ma = max(a, b, i)
            res = ma if ma>res else res
        return res
