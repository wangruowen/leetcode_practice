# https://leetcode.com/problems/elimination-game/description/
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # In forward, first is removed, second becomes the new first
        # In backward,
        # If n is odd, first int is removed
        # second int becomes the new first
        # If n is even, first int is keeped
        # second int is removed
        # Repeat this until only one left
        first, rounds = 1, 1
        while n > 1:
            if rounds % 2 == 1:
                # forward
                first += 2**(rounds-1)
            else:
                # backward
                if n % 2 == 1:
                    # odd
                    first += 2**(rounds-1)
            rounds += 1
            n //= 2
        return first
