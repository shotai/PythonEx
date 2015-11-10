from heapq import *

class MedianFinder:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []
        self.large = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small)==len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small)==len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])
            
  # https://leetcode.com/discuss/64852/ac-python-two-heap-solution-o-log-n-add-o-1-find-388-ms
