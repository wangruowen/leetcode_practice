# https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        if n == 2: return "11"
        s = "11"
        for _ in range(3, n + 1):
            new_s = ""
            i = 0
            while i < len(s):
                start = i
                while i + 1 < len(s) and s[i] == s[i+1]:
                    i += 1
                new_s += str(i - start + 1) + s[i]
                i += 1
            s = new_s
        return s

s = Solution()
print(s.countAndSay(6))
