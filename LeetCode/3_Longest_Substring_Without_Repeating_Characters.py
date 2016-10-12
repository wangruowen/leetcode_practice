class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)

        max_len = 1
        start, end = 0, 1
        char_set = {s[start]: start} # Use hashmap to keep both the char and its index

        while start < len(s) and end < len(s) and start <= end:
            if s[end] not in char_set or char_set[s[end]] < start:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
            else:
                prev_index = char_set[s[end]]
                start = prev_index + 1

            char_set[s[end]] = end
            end += 1

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))