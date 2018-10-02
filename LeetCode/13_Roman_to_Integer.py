# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                   "XL": 40, "L": 50, "XC": 90, "C": 100,
                   "CD": 400, "D": 500, "CM": 900, "M": 1000}
        i = 0
        result = 0
        while i < len(s):
            if s[i:i+2] in mapping:
                result += mapping[s[i:i+2]]
                i += 2
            elif s[i] in mapping:
                result += mapping[s[i]]
                i += 1
        return result
