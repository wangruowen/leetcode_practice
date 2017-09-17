class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        arithmetic_slice_pq_pairs = set()
        p = 0
        while p < len(A) - 2:
            q = p + 2
            while q < len(A):
                if A[q] - A[q - 1] == A[q - 1] - A[q - 2]:
                    arithmetic_slice_pq_pairs.add((p, q))
                    q += 1
                else:
                    # if p + 2 < q:
                    #     arithmetic_slice_pq_pairs.append([p, q - 1])
                    # p = q - 1
                    # p += 1
                    break
            # else:
            #     if p + 2 < q:
            #         arithmetic_slice_pq_pairs.add((p, q - 1))
                # when q == len(A), execute the following
                # Note that the break in Line 20 won't get here
            p += 1

        print(arithmetic_slice_pq_pairs)

        return len(arithmetic_slice_pq_pairs)


s = Solution()
A = [1, 2, 3, 4, 8, 9, 10]
print(s.numberOfArithmeticSlices(A))
