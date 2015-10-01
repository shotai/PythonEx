class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return 0

        res = 0
        k2 =1
        for i in num1[::-1]:
            k1 = 10
            carry=0
            tmpres = 0
            for j in num2[::-1]:
                tmp = int(i)*int(j) + carry
                carry = tmp/k1
                tmpres += (tmp%k1)*(k1/10)
                k1 *= 10
            res += tmpres*k2
            k2 *= 10
            if carry>0:
                res += carry*k2
        return str(res)
