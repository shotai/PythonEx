class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def revert(start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        l = len(nums)
        k %=l
        revert(0, l-1-k)
        revert(l-k,l-1)
        revert(0,l-1)
        
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        while i <k:
            tmp = nums.pop()
            nums.insert(0,tmp)
            i+=1
            
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
