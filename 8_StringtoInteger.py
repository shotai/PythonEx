class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sum = 0
        sign = 1
        i = 0
        if not str:
            return 0
        str = str.strip()
        if str[i] == "-":
            sign = -1
            i = 1
        elif str[i] == "+":
            i = 1
        while i<len(str) and str[i].isdigit():
            sum = sum*10 + int(str[i])
            if (sign*sum)>2147483647 :
                return 2147483647
            if (sign*sum)<-2147483648:
                return -2147483648
            i+=1
        return sign*sum
