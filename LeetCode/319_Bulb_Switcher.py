# https://leetcode.com/problems/bulb-switcher/description/
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [True for _ in range(n)]
        for k in range(2, n + 1):
            bulbs = [not x if (i + 1) % k == 0 else x for i, x in enumerate(bulbs)]
        return sum(bulbs)

    def betterway(self, n):
        return int(n**0.5)

s = Solution()
print(s.bulbSwitch(9999))
