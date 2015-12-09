class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        up = left = 0
        right = len(matrix[0])-1
        down = len(matrix)-1
        direct = 0
        while True:
            if direct==0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            elif direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            elif direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up>down or left>right: return res
            direct = (direct+1)%4
