# https://leetcode.com/problems/possible-bipartition/
from collections import defaultdict

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Bipartite Graph
        # BFS or DFS
        dislike_map = defaultdict(list)
        for a, b in dislikes:
            dislike_map[a].append(b)
            dislike_map[b].append(a)

        # BFS
        g1, g2 = set(), set()
        for i in range(1, N + 1):
            if i not in g1 and i not in g2:
                is_group1 = True
                q = [i]
                while q:
                    new_q = []
                    cur_group = g1 if is_group1 else g2
                    other_group = g2 if is_group1 else g1
                    for i in q:
                        for j in dislike_map[i]:
                            if j in cur_group:
                                return False
                            if j not in other_group:
                                other_group.add(j)
                                new_q.append(j)
                    q = new_q
                    is_group1 = not is_group1
        return True

