class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minp = prices[0]
        fit = 0
        for curr in prices:
            minp = min(minp, curr)
            fit = max(fit, curr-minp)
        return fit
