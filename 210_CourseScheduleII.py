class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for n, pre in prerequisites:
            graph[n].add(pre)
            neighbors[pre].add(n)
        
        stack = [n for n in range(numCourses) if not graph[n]]
        res = []
        while stack:
            node = stack.pop()
            for i in neighbors[node]:
                graph[i].remove(node)
                if not graph[i]:
                    stack.append(i)
            res.append(node)
        return res if len(res)==numCourses else []
