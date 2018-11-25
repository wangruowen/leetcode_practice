# https://leetcode.com/problems/reconstruct-itinerary/
from collections import defaultdict, Counter

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Each pair is an edge, we need to find from JFK as root
        # a path that can cover all airports
        # 1. Note that, it is possible that we fly from JFK to ATL, and then
        # from ATL back to JFK, then we cannot choose JFK to ATL again.
        # 2. It is possible to have multiple tickets from the same src to the same dest
        # We need to keep a counter.
        edges = defaultdict(Counter)
        for src, des in tickets:
            edges[src][des] += 1

        ordered_dest = {}
        for k, v in edges.items():
            ordered_dest[k] = sorted(list(v.keys()))

        def DFS(cur, stack):
            if len(stack) - 1 == len(tickets):
                # No further dest airport
                return stack
            if cur not in ordered_dest:
                return None

            for nei in ordered_dest[cur]:
                if edges[cur][nei] > 0:
                    edges[cur][nei] -= 1
                    stack.append(nei)
                    result = DFS(nei, stack)
                    if result:
                        return result
                    stack.pop()
                    edges[cur][nei] += 1
            return None

        return DFS('JFK', ['JFK'])


s = Solution()
edges = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
edges = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s.findItinerary(edges))
