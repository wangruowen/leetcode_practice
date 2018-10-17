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

    def lengthOfLongestSubstring_v2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        start_ptr, cur_ptr = 0, 1
        max_len = 1
        while cur_ptr < len(s):
            cur_char = s[cur_ptr]
            if cur_char not in s[start_ptr:cur_ptr]:
                max_len = max(max_len, cur_ptr - start_ptr + 1)
            else:
                start_ptr = s[:cur_ptr].rindex(cur_char) + 1
            cur_ptr += 1

        return max_len

    def lengthOfLongestSubstring_v3(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        start = 0
        max_len = 1
        for i in range(1, len(s)):
            if s[i] in s[start:i]:
                # Note that we need to get the rindex of the original string
                start = s[:i].rindex(s[i]) + 1
            else:
                max_len = max(max_len, i - start + 1)

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring_v3("bbtablud"))