# https://leetcode.com/problems/maximum-product-subarray/description/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # local_pos_max, local_neg_min keep track of last max positive and last min negative
        # If the new item is negative, they will switch
        local_pos_max, local_neg_min, global_max = None, None, nums[0]
        for each in nums:
            if each == 0:
                # reset both
                local_pos_max, local_neg_min = None, None
                global_max = max(global_max, each)
            else:
                if each > 0:
                    if local_pos_max is None:
                        local_pos_max = each
                    else:
                        local_pos_max *= each

                    if local_neg_min is not None:
                        local_neg_min *= each
                elif each < 0:
                    old_neg_min = local_neg_min
                    local_neg_min = min(each, (local_pos_max * each) if local_pos_max else each)

                    if old_neg_min is not None:
                        local_pos_max = old_neg_min * each
                    else:
                        local_pos_max = None

                global_max = max(global_max, local_pos_max)

        return global_max

s = Solution()
a = [-2, 0, -1]
print(s.maxProduct(a))