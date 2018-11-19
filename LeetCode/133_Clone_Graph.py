# https://leetcode.com/problems/clone-graph/
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        last, queue, map, new_last_visited = [], [node], {}, set()
        while queue:
            # Now layer-by-layer BFS
            new_queue = []
            for each in queue:
                if each in map:
                    continue
                map[each] = UndirectedGraphNode(each.label)
                for each_nei in each.neighbors:
                    new_queue.append(each_nei)

            # Then fix the neighbor edges for new nodes
            for each_last in last:
                new_last = map[each_last]
                if new_last in new_last_visited:
                    continue
                new_last_visited.add(new_last)
                for each_nei in each_last.neighbors:
                    new_last.neighbors.append(map[each_nei])

            last, queue = queue, new_queue

        return map[node]

    def cloneGraph_v2(self, node):
        if not node:
            return None

        new_node = UndirectedGraphNode(node.label)
        cloned_graph, queue = {node: new_node}, [node]
        while queue:
            cur = queue.pop(0)
            for each_nei in cur.neighbors:
                if each_nei not in cloned_graph:
                    cloned_nei = UndirectedGraphNode(each_nei.label)
                    cloned_graph[each_nei] = cloned_nei
                    queue.append(each_nei)
                cloned_graph[cur].neighbors.append(cloned_graph[each_nei])
        return new_node