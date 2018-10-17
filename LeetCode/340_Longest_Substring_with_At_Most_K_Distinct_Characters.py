# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Base on the template of substring with start and cur pointers
        # https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
        # Time: O(n), Space: O(n)
        max_len = 0
        start, end = 0, 1
        unique_counter = {s[start]: 1}
        while end < len(s):
            if s[end] in unique_counter:
                unique_counter[s[end]] += 1
            else:
                unique_counter[s[end]] = 1
            while len(unique_counter.keys()) > k:
                unique_counter[s[start]] -= 1
                if unique_counter[s[start]] == 0:
                    del unique_counter[s[start]]
                start += 1
            if len(unique_counter.keys()) == k:
                max_len = max(max_len, end - start + 1)
            end += 1
        return max_len

s = Solution()
test = "aaabbb"
k = 3
print(s.lengthOfLongestSubstringKDistinct(test, k))