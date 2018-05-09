# https://leetcode.com/problems/reshape-the-matrix/description/
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row_len, col_len = len(nums), len(nums[0])
        if row_len * col_len != r * c:
            return nums

        result = [[None for _ in range(c)] for _ in range(r)]
        i_n, j_n = 0, 0
        for i in range(row_len):
            for j in range(col_len):
                result[i_n][j_n] = nums[i][j]
                j_n += 1
                if j_n == c:
                    j_n = 0
                    i_n += 1
        return result

s = Solution()
nums = \
[[1,2],
 [3,4]]
r, c = 2, 4
print(s.matrixReshape(nums, r, c))
