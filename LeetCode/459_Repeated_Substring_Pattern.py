# https://leetcode.com/problems/repeated-substring-pattern/description/
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Slow-Fast pointers from the end backward
        # For each step, if the slow and fast pointers point to the same value
        # it is possible that we have substrings
        i = 1
        substrings = []
        while len(s) - 2 * i >= 0:
            slow_ptr = len(s) - i
            fast_ptr = len(s) - 2 * i
            if s[fast_ptr] == s[slow_ptr]:
                if s[fast_ptr:slow_ptr] == s[slow_ptr:]:
                    substrings.append(s[slow_ptr:])
            i += 1

        for each_sub in substrings:
            len_sub = len(each_sub)
            len_s = len(s)
            if len_s % len_sub == 0 and each_sub * (len(s) // len_sub) == s:
                return True

        return False

s = Solution()
input = "abababaabababaabababa"
print(s.repeatedSubstringPattern(input))