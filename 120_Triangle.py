class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle[-1])
        dp = [0 for i in range(l)]
        for row in triangle:
            old = dp[:]
            for i in range(len(row)):
                if i == 0:
                    dp[i] = old[i] + row[i]
                elif i == len(row)-1:
                    dp[i] = old[i-1] + row[i]
                else:
                    dp[i] = min(old[i], old[i-1]) + row[i]
        return min(dp)
