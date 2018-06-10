# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
from Queue import PriorityQueue

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Priority Queue MinHeap
        n = len(matrix)
        queue = PriorityQueue()

        # Init the queue with first row
        for j in range(n):
            queue.put((matrix[0][j], [0, j]))

        # Pop out the first k - 1, and add its down-side one
        for _ in range(k - 1):
            item_val, pos = queue.get()
            if pos[0] == n - 1:
                continue
            queue.put((matrix[pos[0] + 1][pos[1]], [pos[0] + 1, pos[1]]))

        return queue.get()[0]



s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(s.kthSmallest(matrix, k))


