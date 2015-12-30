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
        
    def KSumsolution(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        def ksum(num, k, target):
            i = 0
            if k == 2:
                j = len(num) - 1
                while i<j:
                    if num[i] + num[j] == target:
                        yield (num[i], num[j])
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i<len(num) -k +1:
                    newtarget = target - num[i]
                    for sub in ksum(num[i+1:], k-1, newtarget):
                        yield (num[i],)+sub
                    i += 1
        return [list(t) for t in set(ksum(nums,4, target))]
