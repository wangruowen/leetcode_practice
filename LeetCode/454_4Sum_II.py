# https://leetcode.com/problems/4sum-ii/description/
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # Hash table calculate A and B as a group, then calculate C and D to match
        AB_pair = {}
        for i in range(len(A)):
            for j in range(len(B)):
                AB_pair[A[i] + B[j]] = AB_pair.get(A[i] + B[j], 0) + 1

        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                cd_pair = C[i] + D[j]
                count += AB_pair.get(-cd_pair, 0)

        return count

s = Solution()
ABCD = [
[0,1,-1],
[-1,1,0],
[0,0,1],
[-1,1,1]
]
print(s.fourSumCount(ABCD[0], ABCD[1], ABCD[2], ABCD[3]))
