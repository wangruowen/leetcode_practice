# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
from collections import defaultdict
from collections import Counter

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit_words = ["zero", "one", "two", "three", "four",
                       "five", "six", "seven", "eight", "nine"]
        # Some letters indicate number of certain digits:
        # one digits: 'z':0, 'x':6, 'w':2, 'u':4, 'g':8
        # two digits: 'f':[4, 5], 'h':[3,8], 'v':[5, 7], 's':[6, 7]
        # three digits: 'r':[0,3,4], 't':[2,3,8]
        count = [0] * 10
        for c in s:
            if c == 'z': count[0] += 1
            if c == 'w': count[2] += 1
            if c == 'x': count[6] += 1
            if c == 'g': count[8] += 1
            if c == 'u': count[4] += 1
            if c == 's': count[7] += 1  # 7+6
            if c == 'f': count[5] += 1  # 5+4
            if c == 'h': count[3] += 1  # 3+8
            if c == 'i': count[9] += 1  # 9+5+6+8
            if c == 'o': count[1] += 1  # 1+0+2+4

        # Since the above count duplicated ones
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] -= (count[5] + count[6] + count[8])
        count[1] -= (count[0] + count[2] + count[4])

        result = ""
        for i, c in enumerate(count):
            result += str(i) * c
        return result


s = Solution()
print(s.originalDigits("a"))