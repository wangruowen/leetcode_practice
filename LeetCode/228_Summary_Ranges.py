# https://leetcode.com/problems/summary-ranges/description/
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Two Pointers
        if len(nums) == 0:
            return []

        start = last = 0
        result = []
        i = 1
        while i < len(nums):
            c = nums[i]
            if c != nums[last] + 1:
                if last > start:
                    result.append("%d->%d" % (nums[start], nums[last]))
                else:
                    result.append(str(nums[last]))
                start = i
            last = i
            i += 1

        if last > start:
            result.append("%d->%d" % (nums[start], nums[last]))
        else:
            result.append(str(nums[last]))

        return result

s = Solution()
nums = [0,1,2,4,5,7]
print(s.summaryRanges(nums))