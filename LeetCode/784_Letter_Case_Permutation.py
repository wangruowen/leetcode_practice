# https://leetcode.com/problems/letter-case-permutation/description/
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        lowers = "abcdefghijklmnopqrstuvwxyz"
        uppers = lowers.upper()

        result = [S]
        for i in xrange(len(S)):
            cur = S[i]
            if cur in lowers:
                new_ones = []
                for each in result:
                    new_ones.append(each[:i] + cur.upper() + each[i + 1:])
                result.extend(new_ones)
            elif cur in uppers:
                new_ones = []
                for each in result:
                    new_ones.append(each[:i] + cur.lower() + each[i + 1:])
                result.extend(new_ones)

        return result

s = Solution()
S = "a1b2"
print(s.letterCasePermutation(S))
