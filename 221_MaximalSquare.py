class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(c)] for i in range(r)]
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j]=='1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
                else:
                    dp[i][j]=0
        edge = max([max(i) for i in dp])
        return edge ** 2
