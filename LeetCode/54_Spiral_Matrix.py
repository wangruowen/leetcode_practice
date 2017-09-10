class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n_row = len(matrix)
        if n_row < 1:
            return []
        n_col = len(matrix[0])
        if n_col < 1:
            return []

        return_list = []
        for _round in range((min(n_row, n_col) + 1) / 2):
            i = _round
            for j in range(_round, n_col - _round):
                return_list.append(matrix[i][j])
            for i in range(_round + 1, n_row - _round):
                return_list.append(matrix[i][j])
            if _round + 1 < n_row - _round and _round + 1 < n_col - _round:
                for j in reversed(range(_round, n_col - _round - 1)):
                    return_list.append(matrix[i][j])
                for i in reversed(range(_round + 1, n_row - _round - 1)):
                    return_list.append(matrix[i][j])

        return return_list


s = Solution()
m = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]
print(s.spiralOrder(m))
