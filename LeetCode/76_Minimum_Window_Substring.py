# https://leetcode.com/problems/minimum-window-substring/description/
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Base on the template of substring with start and cur pointers
        # https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
        counter, need_to_match = Counter(t), len(t)
        start = end = result_start = 0
        min_window = float('inf')
        while end < len(s):
            if counter[s[end]] > 0:
                # Current s[end] matches one char in t counter
                need_to_match -= 1
            counter[s[end]] -= 1  # counter[s[end]] could be negative to cover too many chars
            end += 1
            while need_to_match == 0:
                if min_window > end - start:
                    min_window = end - start
                    result_start = start
                # Now we increase start by 1
                counter[s[start]] += 1
                if counter[s[start]] > 0:
                    need_to_match += 1

                # Keep increasing start until need_to_match > 0
                start += 1
        return "" if min_window == float('inf') else s[result_start:result_start + min_window]


