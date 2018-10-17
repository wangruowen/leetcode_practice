# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        i = 0  # i refers to the digit position from right to left
        # Because the input range from 1 to 3999, i is from 0 to 3
        while i < 4:
            if i == 0:
                cur_digit = num % 10
                if cur_digit == 0:
                    pass
                elif cur_digit < 4:
                    result = "I" * cur_digit + result
                elif cur_digit == 4:
                    result = "IV" + result
                elif cur_digit < 9:
                    result = "V" + "I" * (cur_digit - 5) + result
                else:
                    result = "IX" + result
            elif i == 1:
                cur_digit = num % 10
                if cur_digit == 0:
                    pass
                elif cur_digit < 4:
                    result = "X" * cur_digit + result
                elif cur_digit == 4:
                    result = "XL" + result
                elif cur_digit < 9:
                    result = "L" + "X" * (cur_digit - 5) + result
                else:
                    result = "XC" + result
            elif i == 2:
                cur_digit = num % 10
                if cur_digit == 0:
                    pass
                elif cur_digit < 4:
                    result = "C" * cur_digit + result
                elif cur_digit == 4:
                    result = "CD" + result
                elif cur_digit < 9:
                    result = "D" + "C" * (cur_digit - 5) + result
                else:
                    result = "CM" + result
            else:
                cur_digit = num % 10
                if cur_digit == 0:
                    pass
                elif cur_digit < 4:
                    result = "M" * cur_digit + result
            num //= 10
            i += 1
        return result

s = Solution()
print(s.intToRoman(1994))