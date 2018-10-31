# https://leetcode.com/problems/most-profit-assigning-work/
import bisect

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # The higher difficulty doesn't mean the higher the profit
        # each worker first get the subset of allowable difficulty and pick the max profit
        diff_profit = [[v1, v2] for v1, v2 in zip(difficulty, profit)]
        # sort difficulty ascending and sort profit descending
        difficulty.sort()
        diff_profit.sort(key=lambda x: (x[0], -x[1]))
        max_profit_with_diff = []
        cur_max_profit = 0
        for diff, prof in diff_profit:
            cur_max_profit = max(cur_max_profit, prof)
            max_profit_with_diff.append(cur_max_profit)

        max_profit = 0
        for each in worker:
            # Be careful on the bisect_left, it could be 0, could be len(diff)
            diff_index = bisect.bisect_left(difficulty, each)
            if diff_index == 0 and difficulty[0] > each:
                continue
            if diff_index == len(difficulty) or difficulty[diff_index] > each:
                diff_index -= 1
            max_profit += max_profit_with_diff[diff_index]
        return max_profit

s = Solution()
# difficulty = [13, 37, 58]
# profit = [4, 90, 96]
# worker = [34, 73, 45]
# difficulty = [2,4,6,8,10]
# profit = [10,20,30,40,50]
# worker = [4,5,6,7]
difficulty = [85, 47, 57]
profit = [24, 66, 99]
worker = [40, 25, 25]
print(s.maxProfitAssignment(difficulty, profit, worker))

