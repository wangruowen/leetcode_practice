class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        tmp = 1  # forward order to multiply all passed items, and assign to current item
        for i in xrange(len(nums)):
            result.append(tmp)
            tmp *= nums[i]

        tmp = 1  # reset, then backward order to multiply all passed items in the opposite direction
        for i in xrange(1, len(nums) + 1):
            result[-i] *= tmp
            tmp *= nums[-i]

        return result


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
