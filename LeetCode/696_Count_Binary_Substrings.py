# https://leetcode.com/problems/count-binary-substrings/description/
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Two sets switch, Sliding Window
        total_count = 0
        prev_count, curr_count = 0, 0
        for i in range(len(s)):
            if i == 0:
                curr_count = 1
                continue

            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                prev_count = curr_count
                curr_count = 1
            if prev_count > 0:
                prev_count -= 1
                total_count += 1
        return total_count

s = Solution()
a = "01"
print(s.countBinarySubstrings(a))
