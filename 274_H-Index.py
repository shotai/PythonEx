class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n-i):
                return n-i
        return 0
