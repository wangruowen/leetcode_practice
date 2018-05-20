# https://leetcode.com/problems/construct-the-rectangle/description/
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        i = int(math.sqrt(area))
        while area % i != 0:
            i -= 1
        return [area // i, i]

s = Solution()
area = 9999992
print(s.constructRectangle(area))
