# https://leetcode.com/problems/all-paths-from-source-to-target/description/
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS
        result = []
        paths = [[0]]
        while len(paths) > 0:
            new_paths = []
            while len(paths) > 0:
                cur_path = paths.pop(0)
                for each_child in graph[cur_path[-1]]:
                    if each_child == len(graph) - 1:
                        result.append(cur_path + [each_child])
                    else:
                        new_paths.append(cur_path + [each_child])
            paths = new_paths

        return result

    def allPathsSourceTarget_DFS(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def DFS(i, stack, result):
            if i == len(graph) - 1:
                result.append(list(stack))
            for j in graph[i]:
                stack.append(j)
                DFS(j, stack, result)
                stack.pop()
        result = []
        DFS(0, [0], result)
        return result

s = Solution()
graph = [[1,2], [3], [3], []]
print(s.allPathsSourceTarget(graph))