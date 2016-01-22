class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = k%len(nums)
        index = sorted(range(len(nums)), key=lambda x: nums[x], reverse=True)
        return nums[index[k-1]]
    
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for i in nums:
            heapq.heappush(q, i)
        tmp = heapq.nlargest(k, q)
        return tmp[-1]
