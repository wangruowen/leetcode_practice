# https://leetcode.com/problems/utf-8-validation/description/
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        byte_long = 0
        for each in data:
            if byte_long == 0:
                if each & (1 << 7) == 0:
                    byte_long = 1
                elif each & 0b11100000 == 0b11000000:
                    byte_long = 2
                elif each & 0b11110000 == 0b11100000:
                    byte_long = 3
                elif each & 0b11111000 == 0b11110000:
                    byte_long = 4
                else:
                    return False
            else:
                # byte_long is determined by previous byte
                if each >> 6 != 0b10:
                    return False
            byte_long -= 1
        return byte_long == 0
