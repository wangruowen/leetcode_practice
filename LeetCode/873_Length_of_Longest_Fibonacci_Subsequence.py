# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # x_i + x_j = x_k, x_j + x_k = x_q
        # at least find three numbers following the rule
        # DFS / Backtracking
        A_set = {c: i for i, c in enumerate(A)}
        max_length = 0

        def helper(i, j, length):
            nonlocal max_length
            if A[i] + A[j] in A_set:
                k = A_set[A[i] + A[j]]
                helper(j, k, length + 1)
            else:
                max_length = max(max_length, length)

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] in A_set:
                    k = A_set[A[i] + A[j]]
                    helper(j, k, 3)
        return max_length

s = Solution()
A = [1,3,7,11,12,14,18]
print(s.lenLongestFibSubseq(A))


