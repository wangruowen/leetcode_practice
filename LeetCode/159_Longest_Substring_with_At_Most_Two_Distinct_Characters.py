# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-two-distinct-characters.py
#
# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#
from collections import Counter

class Solution:
    # @param s, a string
    # @return an integer
    # Base on the template of substring with start and cur pointers
    # https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
    def lengthOfLongestSubstringTwoDistinct(self, s):
        longest, start, cur, distinct_chars, visited_counter = 0, 0, 0, 0, Counter()
        while cur < len(s):
            if visited_counter[s[cur]] == 0:
                distinct_chars += 1
            visited_counter[s[cur]] += 1
            cur += 1
            while distinct_chars > 2:
                # Shift start pointer, update counter and check distinct_chars
                visited_counter[s[start]] -= 1
                if visited_counter[s[start]] == 0:
                    distinct_chars -= 1
                start += 1

            longest = max(longest, cur - start)
        return longest

    def lengthOfLongestSubstringTwoDistinct_v2(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter()
        start = maxlen = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) > 2:
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    del counter[s[start]]
                start += 1
            maxlen = max(maxlen, i - start + 1)
        return maxlen

s = Solution()
test_str = "eceba"
print(s.lengthOfLongestSubstringTwoDistinct(test_str))
