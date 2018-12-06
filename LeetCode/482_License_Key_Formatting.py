# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = "".join(S.split('-')).upper()
        result = []
        i = len(S)
        while i >= K:
            result.append(S[i-K:i])
            i -= K
        if i > 0:
            result.append(S[:i])
        result.reverse()
        return "-".join(result)
