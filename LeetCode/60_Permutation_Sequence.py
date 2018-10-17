# https://leetcode.com/problems/permutation-sequence/
import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        nums = list(range(1, n+1))  # Build a list and every time remove one item
        k -= 1  # change start index to 0-based
        i = 1
        # k/(n-1)!
        while i <= n:
            cur_fact = math.factorial(n - i)
            cur_i = k // cur_fact
            result += str(nums[cur_i])
            nums.remove(nums[cur_i])
            k = k % cur_fact
            i += 1
        return result

s = Solution()


