# https://www.programcreek.com/2014/10/leetcode-maximum-size-subarray-sum-equals-k-java/
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Because the nums can have negative values, it is not convex or concave
        # it is difficult to use two pointers, so we have to use hash map
        max_len = 0
        sum_to_index = {}
        cur_sum = 0
        for i, c in enumerate(nums):
            cur_sum += c
            if cur_sum == k:
                max_len = max(max_len, i + 1)
            else:
                diff = cur_sum - k  # k = cur_sum - prev_sum
                # check if we already have a sum_so_far that if subtract to k
                if diff in sum_to_index:
                    max_len = max(max_len, i - sum_to_index[diff])
            sum_to_index[cur_sum] = i
        return max_len


s = Solution()
nums = [1,2,-3,3,-1,2,4]
k = 3
print(s.maxSubArrayLen(nums, k))
