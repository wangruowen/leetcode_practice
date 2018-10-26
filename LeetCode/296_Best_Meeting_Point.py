# https://www.programcreek.com/2014/07/leetcode-best-meeting-point-java/
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 2D is the same as 1D for meeting point problem
        x_list, y_list = list(zip(*grid))
        x_list.sort()
        y_list.sort()
        result = 0
        i, j = 0, len(x_list)
        while i < j:
            result += x_list[j] - x_list[i]
            result += y_list[j] - y_list[i]
            i += 1
            j -= 1
        return result



