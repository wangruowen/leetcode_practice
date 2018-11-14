# https://leetcode.com/problems/koko-eating-bananas/
import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        low = math.ceil(sum(piles) / H)  # must eat all within H hours
        high = max(piles)  # Eat max pile in one hour

        def finish_hours(K):
            hours = 0
            for each in piles:
                hours += math.ceil(each / K)
            return hours

        while low <= high:
            mid = (low + high) // 2
            if finish_hours(mid) > H:
                # Need to eat more
                low = mid + 1
            else:
                # Can eat less
                high = mid - 1
        return low