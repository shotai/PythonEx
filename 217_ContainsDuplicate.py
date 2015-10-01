class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nums.sort()
        tmp = nums[0]
        for i in nums[1:]:
            if tmp == i:
                return True
            else:
                tmp=i
        return False
