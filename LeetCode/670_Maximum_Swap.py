# https://leetcode.com/problems/maximum-swap/description/
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        # Try to find the max value since i-th item, from backward
        # e.g., 9 8 3 6 8  <--
        #       9 8 8 8 8
        max_digit_for_each = []
        max_so_far, max_so_far_idx = 0, -1
        for i, c in enumerate(digits):
            if c > max_so_far:
                max_so_far = c
                max_so_far_idx = i
            max_digit_for_each.append([max_so_far, max_so_far_idx])
        # From the opposite direction, find the first max digit bigger than cur item
        for i in range(len(digits) - 1, -1, -1):
            if max_digit_for_each[i][0] > digits[i]:
                j = max_digit_for_each[i][1]
                digits[i], digits[j] = digits[j], digits[i]
                break

        result = 0
        while len(digits) > 0:
            result = result * 10 + digits.pop()
        return result

s = Solution()
# print(s.maximumSwap(98368))
print(s.maximumSwap(92188))
