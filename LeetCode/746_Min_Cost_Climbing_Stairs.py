# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0: return 0
        if len(cost) == 1: return cost[0]
        if len(cost) == 2: return min(cost[0], cost[1])
        # DP
        # total_min_cost[i] is the min cost to reach i-th step, not include i-th cost
        # total[i] = min(total[i - 1] + cost[i - 1], total[i - 2] + cost[i - 2])
        total = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            total[i] = min(total[i - 1] + cost[i - 1], total[i - 2] + cost[i - 2])

        return total[-1]

s = Solution()
# cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(cost))