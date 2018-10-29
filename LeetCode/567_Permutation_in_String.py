# https://leetcode.com/problems/permutation-in-string/
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Sliding Windows Two pointers
        s1_counter = Counter(s1)
        start = 0
        for i, c in enumerate(s2):
            if c in s1_counter:
                s1_counter[c] -= 1

            if i < len(s1) - 1:
                continue

            if s1_counter[c] == 0:
                # Only check the counter when current is 0
                all_zero = True
                for _, v in s1_counter.items():
                    if v != 0:
                        all_zero = False
                        break
                if all_zero:
                    return True
            if s2[start] in s1_counter:
                s1_counter[s2[start]] += 1
            start += 1

        return True if all(v == 0 for _, v in s1_counter.items()) else False

s = Solution()
s1 = "abc"
s2 = "cccccbabbbaaaa"
print(s.checkInclusion(s1, s2))

