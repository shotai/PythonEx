class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def find_left(left, right, n):
            while left<right:
                mid = (left+right)//2
                if n-nums[mid] >= s:
                    left = mid+1
                else:
                    right = mid
            return left
            
        result = len(nums)+1
        for idx, n in enumerate(nums[1:],1):
            nums[idx] = nums[idx-1]+n
        l = 0
        for r, n in enumerate(nums):
            if n>=s:
                l = find_left(l, r, n)
                result = min(result, r-l+1)
        return result if result<=len(nums) else 0
