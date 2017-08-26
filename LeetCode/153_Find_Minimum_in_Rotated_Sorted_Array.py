class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        for i in nums:
            if last == None:
                last = i
            else:
                if last > i:
                    return i
                else:
                    last = i

        return nums[0]

s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
