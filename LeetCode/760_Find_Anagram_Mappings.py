# https://github.com/kamyu104/LeetCode/blob/master/Python/find-anagram-mappings.py
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        B_positions = defaultdict(list)
        for i, b in enumerate(B):
             B_positions[b].append(i)

        mapping = []
        for i, a in enumerate(A):
            mapping.append(B_positions[a].pop())
        return mapping

s = Solution()
A = [12,28,46,28,50]
B = [28, 50, 12, 28, 46]
print(s.anagramMappings(A, B))
