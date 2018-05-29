# https://leetcode.com/problems/happy-number/description/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # The unhappy num has a looping
        visited_set = set()
        digit_sum = sum(int(i) ** 2 for i in list(str(n)))
        while digit_sum not in visited_set:
            visited_set.add(digit_sum)
            digit_sum = sum(int(i) ** 2 for i in list(str(digit_sum)))
        return digit_sum == 1
