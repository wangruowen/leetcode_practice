# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] > A[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
A = [0,2,1,0]
print(s.peakIndexInMountainArray(A))
