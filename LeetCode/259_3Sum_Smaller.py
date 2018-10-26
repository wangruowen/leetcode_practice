# http://www.cnblogs.com/grandyang/p/5235086.html
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    result += k - j  # all i, j, [j+1, k] can be covered
                    j += 1
                else:
                    k -= 1
        return result

s = Solution()
nums = [-2, 0, 1, 3]
target = 2
print(s.threeSumSmaller(nums, target))