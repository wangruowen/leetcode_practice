class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]

        # Subtract the first two layers, now we start from [1, 1]
        rowIndex -= 1
        result_list = [1, 1]

        for _ in xrange(rowIndex):
            left_parent_node = result_list[0]  # For each row, the first node is the first left_parent_node
            for i in xrange(len(result_list) - 1):
                right_parent_node = result_list[i + 1]
                result_list[i + 1] = left_parent_node + right_parent_node
                left_parent_node = right_parent_node
            result_list.append(1)  # Add a new 1 in the end

        return result_list

s = Solution()
print(s.getRow(4))
