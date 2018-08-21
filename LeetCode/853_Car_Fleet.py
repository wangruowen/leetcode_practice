# https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Calculate the time for each car, the order is based on sorted position
        # from far to near
        # from the most near one, keep Current biggest/slowest time of the current car
        # if a little farther car has less or equal time, it means it can catch up
        # the current slowest car
        # Otherwise, the new car becomes the new slowest car, previous slowest car
        # forms its own fleet
        time = [float(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        fleets, cur = 0, 0
        for t in time:
            if t > cur:
                cur = t
                fleets += 1
        return fleets

s = Solution()
target = 10
positions = [0, 4, 2]
speeds = [2, 1, 3]
print(s.carFleet(target, positions, speeds))