# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two Pointers from two sides, also a Greedy algorithm
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                # Because height[i] is used as the height, changing j doesn't help
                # we need a new height[i] to explore new possibilities
                i += 1
            else:
                # Here, height[j] is used as the height, similarly, we need a new j
                j -= 1
        return max_area


