# https://leetcode.com/problems/longest-palindrome/description/
from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_count_map = Counter(s)
        # Keep all even and find the longest odd
        total_len = 0
        has_odd = False
        for c in letter_count_map:
            if letter_count_map[c] % 2 == 0:
                total_len += letter_count_map[c]
            else:
                has_odd = True
                total_len += letter_count_map[c] - 1
        return total_len + int(has_odd)

