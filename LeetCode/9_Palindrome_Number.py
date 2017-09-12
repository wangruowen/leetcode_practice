class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        digit_num = 0
        tmp_x = x
        while tmp_x > 0:
            tmp_x /= 10
            digit_num += 1

        if digit_num % 2 == 1:
            is_odd = True
        else:
            is_odd = False

        new_x = 0
        digit_count = 0
        while digit_count < digit_num / 2:
            one_digit = x % 10
            x /= 10
            new_x = new_x * 10 + one_digit
            digit_count += 1
        if is_odd:
            x /= 10  # remove the in-the-middle one
        if x == new_x:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(-2147447412))


