# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        if len(bits) == 2:
            return True if bits[0] == 0 else False

        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        else:
            return self.isOneBitCharacter(bits[2:])


