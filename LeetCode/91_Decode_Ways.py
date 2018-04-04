# https://leetcode.com/problems/decode-ways/description/
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return len(s)

        # d[i] represents the number of ways to decode till s[i]
        d = [1] * len(s)
        first_2_digit = int(s[0:2])
        if first_2_digit == 10 or first_2_digit == 20:
            d[1] = 1
        elif first_2_digit >= 11 and first_2_digit <= 26:
            d[1] = 2
        elif s[1] == '0':
            return 0
        else:
            d[1] = 1

        for i in xrange(2, len(s)):
            if s[i - 1] == '0':
                if s[i] == '0':
                    return 0  # encounter "00", directly return 0
                d[i] = d[i - 1]
            else:
                last_2_digits = int(s[i - 1:i + 1])
                if last_2_digits == 10 or last_2_digits == 20:
                    d[i] = d[i - 2]
                elif last_2_digits >= 11 and last_2_digits <= 26:
                    d[i] = d[i - 1] + d[i - 2]
                elif s[i] == '0':
                    return 0
                else:
                    d[i] = d[i - 1]

        return d[-1]


s = Solution()
a = "110"
print(s.numDecodings(a))

