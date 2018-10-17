# https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            if carry == 1:
                new_digit = digits[i] + 1
                if new_digit >= 10:
                    digits[i] = new_digit - 10
                    carry = 1
                else:
                    digits[i] = new_digit
                    carry = 0
            else:
                break
            i -= 1
        if i < 0 and carry == 1:
            digits.insert(0, carry)

        return digits