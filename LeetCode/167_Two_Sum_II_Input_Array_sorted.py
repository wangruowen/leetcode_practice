# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]

s = Solution()
a = [2,7,11,15]
target = 9
print(s.twoSum(a, 9))