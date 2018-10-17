# https://leetcode.com/problems/nim-game/
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in range(1, 4):
            return True

        for i in range(1, 4):
            # If the other side can not win after I choose i, then I win.
            if not self.canWinNim(n - i):
                return True

        return False

    def canWinNim_v2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Make it always 4, if the other picks 1, I pick 3, to make it 4
        # If n % 4 == 0, the first hand can never win.
        # If n % 4 != 0, the first hand pick n % 4 to make it n % 4 == 0, then first hand win
        return n % 4 != 0

s = Solution()
print(s.canWinNim(31))