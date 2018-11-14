# https://leetcode.com/problems/k-th-smallest-prime-fraction/
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # 378 Kth Smallest in a Sorted Matrix heap-based solution
        #   |  7    5    2    1
        # --+-------------------
        # 1 | 1/7  1/5  1/2  1/1
        # 2 | 2/7  2/5  2/2  2/1
        # 5 | 5/7  5/5  5/2  5/1
        # 7 | 7/7  7/5  7/2  7/1
        # The K-th element will always be found in the left upper half of the matrix
        # which are smaller than 1
        class Int2D(int):
            # Subclass int class to support getitem, which will make it 2D
            def __getitem__(self, j):
                return float(self) / A[-j-1], [int(self), A[-j-1]]
        return self.kthSmallest(map(Int2D, A), K)


    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Priority Queue MinHeap
        from queue import PriorityQueue
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