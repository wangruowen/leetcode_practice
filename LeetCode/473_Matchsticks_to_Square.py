# https://leetcode.com/problems/matchsticks-to-square/
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or sum(nums) % 4 != 0:
            return False
        nums.sort(reverse=True)
        one_edge_target = sum(nums) // 4
        if max(nums) > one_edge_target:
            return False
        four_edge_sum = [0 for _ in range(4)]

        def DFS(i):
            for j in range(4):
                if four_edge_sum[j] == one_edge_target:
                    continue

                if four_edge_sum[j] + nums[i] <= one_edge_target:
                    four_edge_sum[j] += nums[i]
                    if i == len(nums) - 1:
                        # Last one
                        finish = True
                        for k in range(4):
                            if four_edge_sum[k] != one_edge_target:
                                finish = False
                                break
                        if finish:
                            return True
                    elif DFS(i + 1):
                        return True
                    # Backtrack
                    four_edge_sum[j] -= nums[i]

            return False

        return DFS(0)

s = Solution()
nums =  [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
print(s.makesquare(nums))
