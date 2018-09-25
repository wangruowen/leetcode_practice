# https://leetcode.com/problems/longest-repeating-character-replacement/description/
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Sliding Window
        # Base on the template of substring with start and cur pointers
        # https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
        counter = defaultdict(int)
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            counter[c] += 1
            # The current max count num is the candidate for repeated substr
            # The rest at most k other values can be replaced to the max-count num
            while start < i and i - start + 1 - max(counter.values()) > k:
                # move the start one step forward, reduce the count for the excluded one
                counter[s[start]] -= 1
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len


