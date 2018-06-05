# https://leetcode.com/problems/shuffle-an-array/description/
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig_nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = self.orig_nums[:]
        for i in range(len(ans) - 1):
            j = random.randrange(i, len(ans))
            ans[i], ans[j] = ans[j], ans[i]
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()