# https://leetcode.com/problems/friend-circles/description/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # BFS
        circles = 0
        for i in xrange(len(M)):
            if M[i][i] == 1:
                queue = [i]
                while len(queue) > 0:
                    # Find all i's friends
                    k = queue.pop(0)
                    M[k][k] = -1
                    for j in xrange(len(M)):
                        if M[k][j] == 1:
                            M[k][j] = -1
                            queue.append(j)
                circles += 1

        return circles

    def v2_dfs(self, M, i):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Version 2 DFS
        for j in range(len(M)):
            if M[j][j] == 1 and M[i][j] == 1:
                M[j][j] = -1
                M[i][j] = -1
                self.v2_dfs(M, j)




s = Solution()
M = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
print(s.findCircleNum(M))
