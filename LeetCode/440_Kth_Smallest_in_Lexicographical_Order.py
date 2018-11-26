# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # This is a denary tree (each node has 10 children)
        # Find the kth element is to do a k steps preorder traverse of the tree.
        result = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result + 1]
            # result inclusive, result + 1 exclusive
            while interval[0] <= n:
                count += min(n + 1, interval[1]) - interval[0]
                interval = [x * 10 for x in interval]

            if k >= count:
                k -= count
                # Skip all from result to result + 1, directly start form result + 1
                result += 1
            else:
                # Cannot skip all, we have to move to the next of the result,
                # which is result * 10 and repeat
                result *= 10
                k -= 1
        return result