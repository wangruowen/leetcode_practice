# https://leetcode.com/problems/rotated-digits/description/
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for each in range(1, N + 1):
            rotate_num = 0
            is_valid = True
            i = 0
            tmp = each
            while tmp > 0:
                digit = tmp % 10
                new_digit = 0
                if digit in [0, 1, 8]:
                    new_digit = digit
                elif digit in [2, 5]:
                    new_digit = 2 if digit == 5 else 5
                elif digit in [6, 9]:
                    new_digit = 6 if digit == 9 else 9
                else:
                    is_valid = False
                    break
                rotate_num += new_digit * 10 ** i
                tmp /= 10
                i += 1

            if is_valid and rotate_num != each:
                # print(each)
                count += 1

        return count

s = Solution()
print(s.rotatedDigits(10))
