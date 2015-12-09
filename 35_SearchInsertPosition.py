class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)>>1
            if nums[mid] >= target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1 
        return l
        
    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index,val in enumerate(nums):
            if val>=target:
                return index
        return len(nums)
