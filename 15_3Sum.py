class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp==0:
                    res.append((nums[i], nums[j], nums[k]))
                if tmp>0: #important
                    k-=1
                else:
                    j+=1
        return list(set(res))
