# https://leetcode.com/problems/pascals-triangle/description/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1, 1]

        # Subtract the first two layers, now we start from [1, 1]
        numRows -= 2
        result_list = [1, 1]

        for _ in xrange(numRows):
            left_parent_node = result_list[0]  # For each row, the first node is the first left_parent_node
            for i in xrange(len(result_list) - 1):
                right_parent_node = result_list[i + 1]
                result_list[i + 1] = left_parent_node + right_parent_node
                left_parent_node = right_parent_node
            result_list.append(1)  # Add a new 1 in the end

        return result_list

    def generate_v2(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        numRows -= 1
        result.append([1])
        if numRows == 0:
            return result
        numRows -= 1
        cur_row = [1, 1]
        result.append(cur_row)

        for _ in range(numRows):
            cur_row = list(cur_row)
            last = cur_row[0]
            for i in range(1, len(cur_row)):
                tmp = cur_row[i]
                cur_row[i] += last
                last = tmp
            cur_row.append(last)
            result.append(cur_row)
        return result
