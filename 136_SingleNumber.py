class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in nums[1:]:
            res = res^i
        return res
        
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expect = sum(set(nums))
        res = expect*2-sum(nums)
        return res
