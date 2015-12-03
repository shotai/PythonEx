class Solution(object):
    import itertools
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmpdict = collections.defaultdict(list)
        res = set()
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(nums), 2):
            tmpdict[i1+i2].append({n1, n2})
        
        for t in list(tmpdict.keys()):
            if not tmpdict[target-t]:
                continue
            for pair1 in tmpdict[t]:
                for pair2 in tmpdict[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted(nums[i] for i in pair1 | pair2)))
        return [list(r) for r in res]
