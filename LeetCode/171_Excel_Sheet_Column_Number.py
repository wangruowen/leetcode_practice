# https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for each in s:
            result = result * 26 + ord(each) - ord('A') + 1
        return result
