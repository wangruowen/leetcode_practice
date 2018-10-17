# https://leetcode.com/problems/single-number-iii/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bitwise_xor = 0
        for each in nums:
            bitwise_xor ^= each

        # bitwise_xor = n1 ^ n2
        distinct_bit = 1
        while bitwise_xor & distinct_bit != distinct_bit:
            distinct_bit <<= 1
        # Now bit i is a distinct bit
        # This distinct bit must be either from n1 or from n2

        # Now for second round, let's monitor the bit
        bit_set_group, bit_unset_group = 0, 0
        for each in nums:
            if each & distinct_bit == distinct_bit:
                # Must be 2*k + 1
                bit_set_group ^= each
            else:
                bit_unset_group ^= each

        return [bit_set_group, bit_unset_group]

    def singleNumber_v2(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        distinct_bit = 1
        while distinct_bit & x_xor_y != distinct_bit:
            distinct_bit <<= 1

        x = 0
        for i in nums:
            if i & distinct_bit == distinct_bit:
                x ^= i
        y = x ^ x_xor_y
        return [x, y]

s = Solution()
a = [1,2,1,3,2,5]
print(s.singleNumber(a))
