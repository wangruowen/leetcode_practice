# https://leetcode.com/problems/next-greater-element-ii/description/
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Stack, keep track of decreasing numbers
        stack, result = [0], [-1 for _ in nums]
        for i in range(1, len(nums)):
            if len(stack) == 0 or nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                    result[stack.pop()] = nums[i]
                stack.append(i)

        # After one loop, if len(stack) > 0
        i = 0
        while len(stack) > 0 and i < stack[-1]:
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                result[j] = nums[i]
            i += 1

        return result

s = Solution()
a = [1,2,3,4,3]
print(s.nextGreaterElements(a))


