# https://leetcode.com/problems/maximal-rectangle/

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :param matrix: List[List[str]]
        :return: int
        """
        if len(matrix) == 0: return 0

        cur_height_list = []
        max_area = 0
        for each_row in matrix:
            if len(cur_height_list) == 0:
                # For the first row
                cur_height_list = each_row
            else:
                for i in range(len(each_row)):
                    if each_row[i] == 1:
                        cur_height_list[i] += 1 # It can be just 1, or the height with above consequent 1s
                    else:
                        cur_height_list[i] = 0 # reset to 0

            max_area = max(max_area, self.largestRectangleArea(cur_height_list))

        return max_area


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return heights[0]

        heights.append(0) # Add 0 as the end item to ensure we end in Line 19
        visit_stack = []
        sum = 0
        i = 0
        while i < len(heights):
            if len(visit_stack) == 0 or heights[visit_stack[-1]] < heights[i]:
                visit_stack.append(i)
                i += 1
            else:
                j = visit_stack.pop() # The height
                if len(visit_stack) > 0:
                    length = i - visit_stack[-1] - 1
                else:
                    length = i
                sum = max(sum, heights[j] * length)

        return sum