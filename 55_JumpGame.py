class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            return True
        i = jump = 0
        while i < l and i<=jump:
            if (jump < i+nums[i]):
                jump = i+nums[i]
            if jump>=len(nums)-1:
                return True
            i+=1
        return (jump>=len(nums)-1)
