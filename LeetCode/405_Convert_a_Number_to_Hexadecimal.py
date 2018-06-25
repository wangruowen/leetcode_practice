# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
class Solution(object):
    def toHex_Base16(self, num):
        """
        :type num: int
        :rtype: str
        """
        # num // 16 + num % 16
        maps = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        is_neg = False
        if num < 0:
            is_neg = True
            num = abs(num)
        result = ""
        while num > 0:
            mod_val = num % 16
            if mod_val in maps:
                mod_val = maps[mod_val]
            else:
                mod_val = str(mod_val)
            result += mod_val
            num //= 16
        result = result[::-1]
        print(result)

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Because the num internally is represented as hex
        # we can directly check every 4 bits for 32-bit int
        return "".join(['0123456789abcdef'[(num >> 4 * i) & 0xf] for i in range(8)])[::-1].lstrip('0') or '0'






    @staticmethod
    def twos_complement(input_value, num_bits):
        '''Calculates a two's complement integer from the given input value's bits'''
        mask = 2 ** (num_bits - 1)
        return -(input_value & mask) + (input_value & ~mask)

s = Solution()
print(s.toHex(26))
print(Solution.twos_complement(-26, 32))