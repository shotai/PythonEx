class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlay = min(D-B, H-F, max(D-F,0), max(H-B,0)) * min(C-A, G-E, max(C-E,0), max(G-A,0))
        return (C-A)*(D-B) + (G-E)*(H-F) - overlay
