# https://leetcode.com/problems/bulls-and-cows/description/
from collections import Counter

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_counter = Counter(secret)
        bulls, cows = 0, 0
        # First round, check bulls only
        visited = set()
        for i, c in enumerate(guess):
            if c == secret[i]:
                bulls += 1
                secret_counter[c] -= 1
                visited.add(i)
        # Second round, check cows
        for i, c in enumerate(guess):
            if i not in visited:
                if secret_counter[c] > 0:
                    cows += 1
                    secret_counter[c] -= 1

        return "%dA%dB" % (bulls, cows)
