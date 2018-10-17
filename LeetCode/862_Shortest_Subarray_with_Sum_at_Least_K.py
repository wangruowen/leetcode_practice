# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
from collections import deque

class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # This one cannot handle negative values
        queue, cur_sum, min_len = deque(), 0, float('inf')
        i = 0
        while i < len(A) or cur_sum >= K:
            if i < len(A):
                queue.append(A[i])
                cur_sum += A[i]
                i += 1
            reach_K = False
            while cur_sum >= K:
                reach_K = True
                cur_sum -= queue.popleft()
            if reach_K:
                min_len = min(min_len, len(queue) + 1)

        return min_len if min_len != float('inf') else -1

    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # Prepare a prefix sum list, subarray A[i:j] = prefix[j] - prefix[i]
        prefix_sum = [0]
        cur_sum = 0
        for each in A:
            cur_sum += each
            prefix_sum.append(cur_sum)
        queue = deque()
        min_len = len(A) + 1
        for i in range(len(A) + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= K:
                min_len = min(min_len, i - queue.popleft())
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                # This is caused by a negative value is added
                # The queue is kept as a monotonic increasing queue of prefix_sum
                # If the next prefix_sum is getting smaller, we pop the current ones in the queue
                # it is possible that the queue might be cleaned up
                queue.pop()
            queue.append(i)
        return min_len if min_len < len(A) + 1 else -1

s = Solution()
A = [84,-37,32,40,95]
K = 167
print(s.shortestSubarray(A, K))