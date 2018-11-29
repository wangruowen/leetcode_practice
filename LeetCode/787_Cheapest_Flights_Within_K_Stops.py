# https://leetcode.com/problems/cheapest-flights-within-k-stops/
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # Shortest Path, Dijkstra's Algorithm
        neighbors = defaultdict(dict)
        for u, v, w in flights:
            neighbors[u][v] = w
        q = [(0, src, 0)]

        while q:
            weight, node, stops = heapq.heappop(q)
            # Once popped out, this means this node is marked as visited with minimum weight
            # it is not possible to find a even less weight path for this node
            if node == dst:
                return weight

            if stops <= K:
                # At most K stops in the middle, when reach the dst, it at most has K+1 stops
                # reset this node weight, wait for other paths to reach this
                for v, w in neighbors[node].items():
                    heapq.heappush(q, (weight + w, v, stops + 1))
            # print(q)
        return -1


s = Solution()
n = 3
e = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
# n=4
# e=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
# src=0
# dst=3
# k=1
n=5
e=[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src=0
dst=2
k=2
print(s.findCheapestPrice(n, e, src, dst, k))