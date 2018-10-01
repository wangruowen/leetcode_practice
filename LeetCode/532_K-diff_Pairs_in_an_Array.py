# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        if k == 0:
            # k == 0 is a special case
            # we just need to count the numbers that show up at least twice
            dup_map = {}
            for each in nums:
                if each in dup_map:
                    dup_map[each] = 1
                else:
                    dup_map[each] = 0
            return sum(dup_map.values())


        nums_map = dict.fromkeys(set(nums), 0)
        for each_num in nums_map:
            if (each_num + k) in nums_map:
                nums_map[each_num] += 0.5
            if (each_num - k) in nums_map:
                nums_map[each_num] += 0.5

        return int(sum(nums_map.values()))

    def findPairs_v2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        if k < 0:
            return result
        visited = set()
        if k == 0:
            from collections import Counter
            counter = Counter(nums)
            for _, v in counter.items():
                if v > 1:
                    result += 1
            return result

        for i in nums:
            if i in visited:
                continue
            if i - k in visited:
                result += 1
            if i + k in visited:
                result += 1
            visited.add(i)
        return result

s = Solution()
a=[1, 3, 1, 5, 4]
k=0
print(s.findPairs(a, k))

import collections
