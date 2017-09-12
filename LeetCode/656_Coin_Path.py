import sys


class Solution(object):
    def cheapestJump(self, A, B):
        """
        Using memoization, dp by doing backward counting from the last item. 
        :param A: int list
        :param B: int
        :return: int list
        """
        next = [-1] * len(A)
        dp_min_cost = [0] * len(A)
        for i in reversed(range(len(A) - 1)):
            min_cost = sys.maxint
            j = i + 1
            while j <= i + B and j < len(A):
                if A[j] >= 0:
                    cost = A[i] + dp_min_cost[j]
                    if cost < min_cost:
                        min_cost = cost
                        next[i] = j
                j += 1
            dp_min_cost[i] = min_cost

        result = []
        i = 0
        while i < len(A) and next[i] > 0:
            result.append(i + 1)
            i = next[i]
        if i == len(A) - 1 and A[i] >= 0:
            result.append(i + 1)
        else:
            return []
        return result


s = Solution()
A = [1, 2, 4, -1, 2]
B = 2
print(s.cheapestJump(A, B))
