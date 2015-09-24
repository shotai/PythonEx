class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = ''.join(map(str, digits))
        return map(int, str(int(tmp)+1))
