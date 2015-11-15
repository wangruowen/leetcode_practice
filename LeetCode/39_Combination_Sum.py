__author__ = 'ruowen.wang'
# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def _combination(self, candidates, target, exist_comb=[]):
        for i in range(len(candidates)):
            each_num = candidates[i]
            remain_target = target - each_num
            if remain_target == 0:
                # succeed
                exist_comb_copy = list(exist_comb)
                exist_comb_copy.append(each_num)
                self.success_comb.append(exist_comb_copy)
                return
            if remain_target < 0:
                return
            if len(exist_comb) == 0:
                exist_comb_copy = [each_num]
            else:
                exist_comb_copy = list(exist_comb)
                exist_comb_copy.append(each_num)
            self._combination(candidates[i:], remain_target, exist_comb_copy)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.success_comb = []
        self._combination(sorted(candidates), target)
        return self.success_comb

s = Solution()
print(s.combinationSum([2,3,6,7], 7))