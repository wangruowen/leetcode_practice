# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
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

a = [2, 4]
s = Solution()
print(s.largestRectangleArea(a))