# https://leetcode.com/problems/repeated-string-match/description/
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # First, Double A, then B should be starts from some offset to the end of the first A,
        # and then the following B should be just repeating of A
        if B in A:
            return 1
        if B in A * 2:
            return 2

        start = -1
        for i in range(len(A)):
            if A[i:] == B[:len(A) - i]:
                start = i
                break

        if start == -1:
            return -1

        new_start = len(A) - start
        repeat_count = len(B[new_start:]) // len(A)
        if A * repeat_count != B[new_start:new_start + repeat_count * len(A)]:
            return -1
        remain = len(B[new_start:]) % len(A)
        if remain > 0:
            if not A.startswith(B[new_start + repeat_count * len(A):]):
                return -1
            repeat_count += 1

        return repeat_count + 1

s = Solution()
A = "aabaa"
B = "aaab"
print(s.repeatedStringMatch(A, B))