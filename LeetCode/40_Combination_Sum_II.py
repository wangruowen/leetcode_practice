# https://leetcode.com/problems/combination-sum-ii/description/
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Backtrack
        self.total_set = []
        self.helper(sorted(candidates), 0, target, [])

        return self.total_set

    def helper(self, candidates, index, target, cur_set):
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                new_set = cur_set[:]
                new_set.append(target)
                self.total_set.append(new_set)
                break
            elif i > index and candidates[i] == candidates[i - 1]:
                # Same number, already analyzed
                continue
            else:
                cur_set.append(candidates[i])
                self.helper(candidates, i + 1, target - candidates[i], cur_set)
                cur_set.pop()


s = Solution()
c = [10,1,2,7,6,1,5]
t = 8
print(s.combinationSum2(c, t))
