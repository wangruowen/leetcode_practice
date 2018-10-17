# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in zip(*strs):
            is_same = True
            for j in i:
                if j != i[0]:
                    is_same = False
                    break
            if not is_same:
                return result
            result += i[0]

        return result

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))