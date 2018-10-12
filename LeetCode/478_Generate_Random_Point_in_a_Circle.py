# https://leetcode.com/problems/generate-random-point-in-a-circle/
import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x = (random.random() * 2 - 1) * self.r + self.x
            y = (random.random() * 2 - 1) * self.r + self.y
            if (x - self.x) ** 2 + (y - self.y) ** 2 < self.r ** 2:
                return [x, y]

# Your Solution object will be instantiated and called as such:
obj = Solution(10, 5, -7.5)
param_1 = obj.randPoint()
print(param_1)