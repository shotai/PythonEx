class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                helper(i+1, valuelist+[nums[i]])
        res = []
        if not nums:
            return res
        nums.sort()
        helper(0, [])
        return res
