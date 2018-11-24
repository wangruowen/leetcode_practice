# https://leetcode.com/problems/open-the-lock/
from collections import deque


class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # BFS
        q = deque(["0000"])
        deadends, visited = set(deadends), set(q)
        if "0000" in deadends:
            return -1

        def get_neighbors(digits):
            nei = []
            for i in range(4):
                digit = int(digits[i])
                for d in [(digit + 1) % 10, (digit - 1) % 10]:
                    nei.append(digits[:i] + str(d) + digits[i + 1:])
            return nei

        moves = 0
        while q:
            new_q = deque()
            while q:
                cur = q.popleft()
                if cur == target:
                    return moves
                for each in get_neighbors(cur):
                    if each not in deadends and each not in visited:
                        visited.add(each)
                        new_q.append(each)
            moves += 1
            q = new_q
        return -1
