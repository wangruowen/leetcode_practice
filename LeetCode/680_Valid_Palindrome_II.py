# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If it is already palindrome, just return True
        if s == s[::-1]:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # Either delete s[i] or s[j] and the rest should be palindrome
                return self.isPalindrome(s[i + 1:j + 1]) or self.isPalindrome(s[i:j])

        return True

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
a = \
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

print(s.validPalindrome(a))