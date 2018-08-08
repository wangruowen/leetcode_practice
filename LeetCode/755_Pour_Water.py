# https://github.com/kamyu104/LeetCode/blob/master/Python/pour-water.py
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        # At index K, find lowest left and lowest right, fill the lowest one
        for _ in range(V):
            i, j = K - 1, K + 1
            lowest_left_i, lowest_right_j = i, j
            while i >= 0:
                if heights[lowest_left_i] > heights[i]:
                    lowest_left_i = i
                i -= 1
            while j < len(heights):
                if heights[lowest_right_j] > heights[j]:
                    lowest_right_j = j
                j += 1
            if heights[lowest_left_i] >= heights[lowest_right_j]:
                most_lowest_idx = lowest_right_j
            else:
                most_lowest_idx = lowest_left_i
            heights[most_lowest_idx] += 1

        return heights