# https://leetcode.com/problems/magical-string/description/
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 2 2
        # 1 2 2 1 1
        # 1 2 2 1 1 2 1
        # 1 2 2 1 1 2 1 2 2 1
        # 1 2 2 1 1 2 1 2 2 1 2 2 1 1 2
        # ...
        # Every time, we need to generate the extra part
        if n == 0:
            return 0
        if n <= 3:
            return 1
        last = [2]
        return self._helper(n - 3, last, 1)

    def _helper(self, rest_n, last, one_count):
        if rest_n == 0:
            return one_count

        cur_digit = 1 if last[-1] == 2 else 2
        new_generated = []
        while rest_n > 0 and len(last) > 0:
            num = last.pop(0)
            if num <= rest_n:
                # print(num)
                new_generated.extend([cur_digit] * num)
                rest_n -= num
                if cur_digit == 1:
                    one_count += num
            else:
                if cur_digit == 1:
                    one_count += rest_n
                return one_count
            cur_digit = 1 if cur_digit == 2 else 2

        # print(new_generated)

        if rest_n > 0:
            return self._helper(rest_n, new_generated, one_count)
        return one_count

s = Solution()
print(s.magicalString(6))
