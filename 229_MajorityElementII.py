class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1, num2 = 0, 0
        c1, c2 = 0, 0
        r = []
        for i in nums:
            if i == num1:
                c1 += 1
            elif i == num2:
                c2 += 1
            elif c1 == 0:
                num1 = i
                c1 = 1
            elif c2 == 0:
                num2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = 0
        c2 = 0
        for j in nums:
            if j == num1:
                c1 += 1
            elif j == num2:
                c2 += 1
        l = len(nums)
        if c1 > l/3:
            r.append(num1)
        if c2 > l/3:
            r.append(num2)
        return r
