# https://leetcode.com/problems/brick-wall/description/
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        row_len = sum(wall[0])
        gap_count = {}
        max_count = 0
        for row in wall:
            cumulate_sum = 0
            for each in row:
                cumulate_sum += each
                if cumulate_sum < row_len:
                    if cumulate_sum in gap_count:
                        gap_count[cumulate_sum] += 1
                    else:
                        gap_count[cumulate_sum] = 1
                    max_count = max(max_count, gap_count[cumulate_sum])
        return len(wall) - max_count

s = Solution()
wall = [[6, 2, 2], [1, 4, 4, 1], [2, 5, 3]]
print(s.leastBricks(wall))