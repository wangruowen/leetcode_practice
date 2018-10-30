# https://leetcode.com/problems/unique-letter-string
class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Based on this
        # https://leetcode.com/problems/unique-letter-string/discuss/128952/One-pass-O(N)-Straight-Forward
        alphabet_pos = [[-1, -1] for _ in range(26)]
        # For each encountered letter, keep its last two same letter positions
        # the diff distance is the possible ways to make it unique
        result = 0
        for i, c in enumerate(S):
            idx = ord(c) - ord('A')
            i1, i2 = alphabet_pos[idx]
            result += (i2 - i1) * (i - i2)
            alphabet_pos[idx] = [i2, i]
        for i1, i2 in alphabet_pos:
            result += (i2 - i1) * (len(S) - i2)
        return result

s = Solution()
print(s.uniqueLetterString("ABC"))


