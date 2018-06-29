class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return [1, 2] if 1 in nums else [2, 1]

        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                duplicate_num = nums[i]
                break
        missing_num = (1 + n) * n / 2 - (sum(nums) - duplicate_num)

        return [duplicate_num, missing_num]

    def findErrorNums2(self, nums):
        # For each visited, we mark the corresponding indexed num as negative
        dup = None
        for i, c in enumerate(nums):
            if c < 0:
                c = abs(c)

            # Mark c-1 th num negative
            if nums[c - 1] < 0:
                # Already visited
                dup = c
            else:
                nums[c - 1] *= -1
        miss = None
        for i, c in enumerate(nums):
            if c > 0:
                miss = i + 1
        return dup, miss





s = Solution()
print(s.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))
