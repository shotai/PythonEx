class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if abs(dividend)<abs(divisor):
            return 0
        count = 0
        res = 0
        sum = 0
        a = abs(dividend)
        b = abs(divisor)
        while a>=b:
            sum = b
            count =1
            while sum+sum<=a:
                sum += sum
                count += count
            a-=sum
            res += count
        if (dividend <0 and divisor >0) or (dividend>0 and divisor < 0):
            res = 0-res
        if res>= 2147483647:
            res = 2147483647
        return res
