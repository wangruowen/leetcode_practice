# https://leetcode.com/problems/contiguous-array/description/
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Tricky Explained in https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
        count = 0
        count_dict = {0: -1}
        max_len = 0
        for i, c in enumerate(nums):
            count += 1 if c == 1 else -1
            if count in count_dict:
                max_len = max(max_len, i - count_dict[count])
            else:
                count_dict[count] = i
        return max_len
