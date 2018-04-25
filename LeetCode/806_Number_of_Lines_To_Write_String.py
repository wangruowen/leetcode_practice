# https://leetcode.com/problems/number-of-lines-to-write-string/description/
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return [0, 0]
        line_count, one_line_count = 1, 0
        for each in S:
            one_line_count += widths[ord(each) - ord('a')]
            if one_line_count > 100:
                line_count += 1
                one_line_count = widths[ord(each) - ord('a')]

        return [line_count, one_line_count]

s = Solution()
a = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
b = "bbbcccdddaaa"
print(s.numberOfLines(a, b))