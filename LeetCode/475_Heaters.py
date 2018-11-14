# https://leetcode.com/problems/heaters/description/
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # For each house, find its nearest heater using Binary Search
        houses.sort()
        heaters.sort()
        max_radius = 0
        for each_house in houses:
            max_radius = max(max_radius, self._find_closest_heater_dist(each_house, heaters, 0, len(heaters) - 1))
        return max_radius

    def _find_closest_heater_dist(self, house_pos, heaters, start, end):
        if start == end or start + 1 == end:
            return min(abs(house_pos - heaters[start]), abs(heaters[end] - house_pos))
        mid = (start + end) / 2
        if house_pos < heaters[mid]:
            end = mid
        elif house_pos > heaters[mid]:
            start = mid
        else:
            return 0
        return self._find_closest_heater_dist(house_pos, heaters, start, end)

    def findRadius_bisect(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        import bisect
        # For each house, find tis nearest warmer, calculate the radius,
        # and return the max radius
        houses.sort()
        heaters.sort()
        max_radius = float('-inf')
        for each in houses:
            i = bisect.bisect(heaters, each)
            if i == 0:
                radius = abs(heaters[i] - each)
            elif i == len(heaters):
                radius = abs(heaters[-1] - each)
            else:
                radius = min(each - heaters[i - 1], heaters[i] - each)
            max_radius = max(max_radius, radius)
        return max_radius

s = Solution()
# houses = [1,1,1,1,1,1,999,999,999,999,999]
# heaters = [499,500,501]
houses = [1,2,3]
heaters = [2]
print(s.findRadius(houses, heaters))
