class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def helper(n):
            if n<20:
                return to19[n-1:n]
            if n<100:
                return [tens[(n/10-2)]]+helper(n%10)
            if n<1000:
                return [to19[(n/100-1)]]+['Hundred']+helper(n%100)
            for k, v in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n< 1000**(k+1):
                    return helper(n/1000**k)+[v]+helper(n%1000**k)
        return ' '.join(helper(num)) or 'Zero'
