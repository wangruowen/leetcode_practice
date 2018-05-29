# https://leetcode.com/problems/combination-sum-iii/description/
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Backtracking
        total_combins = []
        self.helper(k, n, [], range(1, 10), total_combins)
        return total_combins

    def helper(self, k, n, cur_combin, avail_nums, total_combins):
        if k == 0:
            return
        for i in range(len(avail_nums)):
            num = avail_nums[i]
            if k == 1 and num == n:
                cur_combin.append(num)
                total_combins.append(list(cur_combin))
                cur_combin.pop()
                return
            if num < n:
                cur_combin.append(num)
                self.helper(k - 1, n - num, cur_combin, avail_nums[i + 1:], total_combins)
                cur_combin.pop()

s = Solution()
k = 3
n = 9
print(s.combinationSum3(k,n))