# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
from collections import Counter, defaultdict

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # First, count, if there are some chars whose total count < k,
        # then the string has to be splitted by those <k chars
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


s = Solution()
s_input = "zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee"
k = 10
# s_input="bbaaacbd"
# k = 3
print(s.longestSubstring(s_input, k))


