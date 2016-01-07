
class Solution:
    """
        :type n: int
        :rtype: str
        """
    def countAndSay(self, n):
        s = '1'
        for i in range(n-1):
            prev = newS = ''
            num = 0
            for curr in s:
                if prev != '' and prev != curr:
                    newS += str(num)+prev
                    num = 1
                else:
                    num += 1
                prev = curr
            newS+=str(num) + prev
            s = newS
        return s
