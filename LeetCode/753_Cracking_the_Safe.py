# https://leetcode.com/problems/cracking-the-safe/
class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # DFS with sliding window to iterate all the permutations available
        # For example, n = 2, k = 2
        # 00     visited = {00}
        #  01    visited = {00, 01}
        #   10   visited = {00, 01, 10}
        #    01    01 is already visited, backtrack
        #    00    00 is already visited, backtrack
        #   11   visited = {00, 01, 11}
        #    10  visited = {00, 01, 11, 10}
        # result: 00110
        def DFS(passwd, visited, stack):
            if len(visited) == k ** n:
                # all permutations of n digits are visited
                return True

            for i in range(k):
                new_pass = passwd[1:] + str(i)
                if new_pass not in visited:
                    visited.add(new_pass)
                    stack.append(str(i))
                    if DFS(new_pass, visited, stack):
                        return True
                    visited.remove(new_pass)
                    stack.pop()
            return False

        start_pass = "0" * n
        visited = set([start_pass])
        stack = ['0' for _ in range(n)]
        DFS("0" * n, visited, stack)
        return "".join(stack)


s = Solution()
n = 3
k = 2
print(s.crackSafe(n, k))

