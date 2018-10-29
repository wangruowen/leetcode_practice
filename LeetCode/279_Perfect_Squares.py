# https://leetcode.com/problems/perfect-squares/
from queue import deque

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS
        square_nums = [i ** 2 for i in range(1, int(n ** 0.5) + 1)][::-1]
        # print(square_nums)

        queue = deque([n])
        round = 0
        while queue:
            round += 1
            new_queue = deque()
            while queue:
                cur_n = queue.popleft()

                for each in square_nums:
                    if each <= cur_n:
                        if each == cur_n:
                            return round
                        new_queue.append(cur_n - each)
            queue = new_queue

s = Solution()
print(s.numSquares(7168))
