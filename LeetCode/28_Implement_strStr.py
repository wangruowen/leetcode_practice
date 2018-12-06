# https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
            else:
                # reset j
                # also rollback i
                i -= j
                j = 0
            i += 1
        return -1

    def strStr_v2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Just do sliding window
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

s = Solution()
h = "mississippi"
n = "issip"
print(s.strStr(h, n))