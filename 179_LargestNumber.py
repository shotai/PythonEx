class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(nums, cmp = lambda a,b:cmp(str(b)+str(a), str(a)+str(b)))
        s = ''.join(map(str,nums))
        return s if s.replace('0', '')!='' else '0'
