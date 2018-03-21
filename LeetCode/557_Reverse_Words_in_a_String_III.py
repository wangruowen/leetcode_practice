# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split()
        return " ".join(map(lambda x: x[::-1], tokens))

s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))