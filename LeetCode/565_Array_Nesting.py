# https://leetcode.com/problems/array-nesting/description/
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DFS S[0] = {A[0], S[A[0]]}
        S = [-1 for _ in range(len(nums))]
        max_len = 0
        for i, a in enumerate(nums):
            if S[i] > 0:
                continue
            k = i
            visited_indices = [k]
            while nums[k] != i:
                k = nums[k]
                visited_indices.append(k)
            for each in visited_indices:
                S[each] = len(visited_indices)
            max_len = max(max_len, S[i])
        return max_len

s = Solution()
nums = [5,4,0,3,1,6,2]
print(s.arrayNesting(nums))