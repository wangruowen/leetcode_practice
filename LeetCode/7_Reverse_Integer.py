class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_SIGNED_INT = 0x7fffffff
        MIN_SIGNED_INT = -MAX_SIGNED_INT - 1

        str_x = str(x)
        if str_x[0] == "-":
            is_negative = True
            str_x = str_x[1:]
        else:
            is_negative = False

        reverse_x = str_x[::-1]
        if is_negative:
            reverse_x = int("-" + reverse_x)
            if reverse_x < MIN_SIGNED_INT:
                reverse_x = 0
        else:
            reverse_x = int(reverse_x)
            if reverse_x > MAX_SIGNED_INT:
                reverse_x = 0

        return reverse_x

s = Solution()
print(s.reverse("-123"))