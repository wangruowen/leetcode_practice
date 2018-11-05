# https://leetcode.com/problems/count-of-range-sum/description/
class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Merge Sort -based Divide and Conquer
        # Now if we break our original input array into two subarrays,
        # [0, m] and [m+1, n-1] with m = (n-1)/2,
        # our original problem can be divided into three parts,
        # depending on the values of i1 and i2.
        # If i1 and i2 are both from the first subarray [0, m],
        # we have a subproblem T(0, m);
        # if i1 and i2 are both from the second subarray,
        # we have a subproblem T(m+1, n-1);
        # if i1 is from the first subarray and i2 from the second (note we assume i1 <= i2,
        # therefore we don't have the other case with i2 from first subarray and i1 from second),
        # then we have a new problem which I define as C. In summary we should have:
        #
        # T(0, n-1) = T(0, m) + T(m+1, n-1) + C
        prefix = [0]
        for each in nums:
            prefix.append(prefix[-1] + each)

        def count_using_mergesort(lo, hi):
            mid = (lo + hi) // 2  # lo inclusive, hi exclusive
            if mid == lo:
                return 0

            # First recursive count subproblems
            count = count_using_mergesort(lo, mid) + count_using_mergesort(mid, hi)

            # Now we cover cases that start point from lo, mid, end point from mid, hi
            # range is prefix[end] - prefix[start]
            lower_bound_end = upper_bound_end = mid
            for start in prefix[lo:mid]:
                # Note that, prefix[lo:mid] has already been sorted by Line 21,
                # that's why we can do the following lower bound and upper bound search
                while lower_bound_end < hi and prefix[lower_bound_end] - start < lower:
                    lower_bound_end += 1
                while upper_bound_end < hi and prefix[upper_bound_end] - start <= upper:
                    upper_bound_end += 1
                count += upper_bound_end - lower_bound_end

            # sort the prefix from lo to hi for caller's prefix[lo:mid]
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count
        return count_using_mergesort(0, len(prefix))

s = Solution()
nums = [-2, 5, -1]
lower = -2
upper = 2
print(s.countRangeSum(nums, lower, upper))