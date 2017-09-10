__author__ = 'Ruowen'
# https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return None
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            t2, t3, t5 = 2 * ugly_nums[i2], 3 * ugly_nums[i3], 5 * ugly_nums[i5]
            chosen = min(t2, t3, t5)
            if chosen == t2:
                i2 += 1
            if chosen == t3:
                i3 += 1
            if chosen == t5:
                i5 += 1
            ugly_nums.append(chosen)
        return ugly_nums[-1]


s = Solution()
print(s.nthUglyNumber(7))