class Solution(object):
    def permuteUnique_iter(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret = [[]]
        for n in nums:
            tmp_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i<l and seq[i] == n:
                        break
                    tmp_ret.append(seq[:i] + [n] + seq[i:])
                ret = tmp_ret
        return ret
        
    def helper(self, start, end, nums):
        if(start==end-1):
            Solution.res.append(list(nums))
        visited = set()
        for k in range(start,end):
            if nums[k] not in visited:
                nums[start], nums[k] = nums[k], nums[start]
                self.helper(start+1, end, nums)
                nums[start], nums[k] = nums[k], nums[start]
                visited.add(nums[k])
    def permuteUnique(self, nums):
        nums.sort()
        Solution.res = []
        self.helper(0,len(nums),nums)
        return Solution.res
