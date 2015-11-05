class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        l, r, water, minheight = 0, len(height)-1, 0, 0
        
        while l<r:
            while l<r and height[l]<=minheight:
                
                water += minheight-height[l]
                l += 1
                
            while l<r and height[r]<=minheight:
                water += minheight-height[r]
                r -= 1
            
            minheight = min(height[r], height[l])
            
        return water
