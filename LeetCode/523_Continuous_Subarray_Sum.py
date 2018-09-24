# https://leetcode.com/problems/continuous-subarray-sum/
from collections import defaultdict

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        if k == 0:
            last = -1
            for cur in nums:
                if last == cur == 0:
                    return True
                last = cur
            return False

        # If subarray (prefix[j] - prefix[i]) % k == 0
        # Then prefix[j] % k == prefix[i] % k when j > i + 1
        prefix_mod_k = defaultdict(list)
        cur_sum = 0
        prefix_mod_k[0].append(0)
        for i, c in enumerate(nums):
            cur_sum += c
            if cur_sum % k in prefix_mod_k:
                for j in prefix_mod_k[cur_sum % k]:
                    if i > j:
                        # print(i, j)
                        return True
            prefix_mod_k[cur_sum % k].append(i+1)
        return False

s = Solution()
nums = [2,4]
k = 6
print(s.checkSubarraySum(nums, k))
