# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/
class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        # Count 5, the number of zeros is the number of 5
        # https://mathoverflow.net/questions/16254/counting-trailing-zeros-for-factorials/16255#16255
        # (5*K)! must have more than K zeros
        def numOfZerosFactorialN(n):
            count = 0
            while n > 0:
                count += n // 5
                n //= 5
            return count

        # print(numOfZerosFactorialN(25))

        def binarySearch(k):
            left, right = 0, 5*(k+1)  # inclusive right
            while left < right:
                mid = (left + right) // 2
                num_of_zeros = numOfZerosFactorialN(mid)
                # print("mid = %d, zeros = %d" % (mid, num_of_zeros))
                if num_of_zeros >= k:
                    right = mid
                else:
                    left = mid + 1
            if num_of_zeros == k:
                return right
            else:
                return 0

        x, y = binarySearch(K), binarySearch(K - 1)
        if x == 0:
            return 0
        else:
            return x - y

s = Solution()
print(s.preimageSizeFZF(5))






