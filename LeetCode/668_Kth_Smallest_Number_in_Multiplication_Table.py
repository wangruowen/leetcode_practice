# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # One way is to use PriorityQueue similar as 378
        # The other way is to use Binary Search from 1 to m*n
        # Image a flattened list of the multiplication matrix
        # i, 2*i, 3*i, ... n*i count how many of them are smaller than mid
        l, h = 1, m * n
        while l < h:
            mid = (l + h) // 2
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)
            if cnt >= k:
                h = mid
            elif cnt < k:
                l = mid + 1
        return l


