class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start,cur = -1,0
        while cur<len(nums):
            if not nums[cur]==0:
                start +=1
                nums[cur], nums[start] = nums[start], nums[cur]
            cur += 1
        return
