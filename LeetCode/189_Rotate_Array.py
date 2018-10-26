# https://leetcode.com/problems/rotate-array/description/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # DFS based in-place modification
        k %= len(nums)
        i, cur_val = 0, nums[0]
        visited = set()
        while i < len(nums):
            if i not in visited:
                # i -> (i + k) % len(nums)
                visited.add(i)
                new_i = (i + k) % len(nums)
                tmp = nums[new_i]
                nums[new_i] = cur_val
                i, cur_val = new_i, tmp
            else:
                i += 1
                if i < len(nums):
                    cur_val = nums[i]
                else:
                    break

        # return nums

s = Solution()
nums = [-1,-100,3,99]
k = 2
s.rotate(nums, k)
print(nums)