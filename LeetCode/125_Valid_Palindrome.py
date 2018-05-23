# https://leetcode.com/problems/valid-palindrome/description/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        s = s.lower()
        while i <= j < len(s):
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i < len(s) and j >= 0:
                if s[i] != s[j]:
                    return False
            elif (i == len(s) and j >= 0) or (i < len(s) and j < 0):
                return False
            i += 1
            j -= 1
        return True


s = Solution()
a = "."
print(s.isPalindrome(a))