# https://leetcode.com/problems/flood-fill/description/
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # BFS
        queue = [(sr, sc)]
        oldColor = image[sr][sc]
        while len(queue) > 0:
            cur_sr, cur_sc = queue.pop(0)
            if image[cur_sr][cur_sc] == newColor:
                continue
            image[cur_sr][cur_sc] = newColor

            if cur_sr > 0 and image[cur_sr - 1][cur_sc] == oldColor:
                queue.append((cur_sr - 1, cur_sc))
            if cur_sr < len(image) - 1 and image[cur_sr + 1][cur_sc] == oldColor:
                queue.append((cur_sr + 1, cur_sc))
            if cur_sc > 0 and image[cur_sr][cur_sc - 1] == oldColor:
                queue.append((cur_sr, cur_sc - 1))
            if cur_sc < len(image[0]) - 1 and image[cur_sr][cur_sc + 1] == oldColor:
                queue.append((cur_sr, cur_sc + 1))

        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2
s = Solution()
print(s.floodFill(image, sr, sc, newColor))
