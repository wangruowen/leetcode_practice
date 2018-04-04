# https://leetcode.com/problems/single-number-ii/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        In [1]: a = 1234

In [2]: bin(a)
Out[2]: '0b10011010010'

In [3]: a & 0x1
Out[3]: 0

In [4]: a & 0x11
Out[4]: 16

In [5]: bin(a & 0x11)
Out[5]: '0b10000'

In [6]: bin(a & 0b11)
Out[6]: '0b10'

In [7]: int(bin(a & 0b11))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-7-3cb6396c2f14> in <module>()
----> 1 int(bin(a & 0b11))

ValueError: invalid literal for int() with base 10: '0b10'

In [8]: int(bin(a & 0b11), 2)
Out[8]: 2

In [9]: int(bin(a & 0b111), 2)
Out[9]: 2

In [10]: a
Out[10]: 1234

In [11]: bin(a)
Out[11]: '0b10011010010'

In [12]: int(bin(a & 0b11111), 2)
Out[12]: 18

In [13]: bin(a & 0b11111)
Out[13]: '0b10010'

In [14]:

        """
        bitwise_stats = [0] * 32
        mask = (1 << 32) - 1  # 0xffffffff
        for each in nums:
            for i in range(32):
                bitwise_stats[i] += (mask & each) >> i & 0b1
            # print(bitwise_stats)

        for i in range(32):
            bitwise_stats[i] %= 3

        is_neg = bitwise_stats[31] == 1

        # print(bitwise_stats)
        result = int("0b" + "".join(map(lambda x: str(x), bitwise_stats[::-1])), 2)
        if is_neg:
            result = ~result & 0xffffffff
            result = -result - 1
        return result


s = Solution()
a = [-2, -2, -2, -4]
print(s.singleNumber(a))

