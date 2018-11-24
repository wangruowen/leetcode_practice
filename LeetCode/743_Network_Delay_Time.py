# https://leetcode.com/problems/network-delay-time/
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Dijkstra Algorithm
        neighbors = defaultdict(dict)
        for u, v, w in times:
            neighbors[u][v] = w

        q = [(0, K)]
        node_path_w = {i: float('inf') if i != K else 0 for i in range(1, N+1)}
        while q:
            cur_w, cur = heapq.heappop(q)
            for v, w in neighbors[cur].items():
                if cur_w + w < node_path_w[v]:
                    node_path_w[v] = cur_w + w
                    heapq.heappush(q, (node_path_w[v], v))
        # print(node_path_w)
        max_path = max(node_path_w.values())
        return max_path if max_path < float('inf') else -1

s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
times = [[1,2,1]]
N = 2
K = 2
print(s.networkDelayTime(times, N, K))