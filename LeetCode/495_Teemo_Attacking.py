# https://leetcode.com/problems/teemo-attacking/description/
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_poison_time = 0
        if len(timeSeries) == 0:
            return 0
        i = 1
        while i < len(timeSeries):
            if timeSeries[i] - timeSeries[i - 1] < duration:
                total_poison_time += timeSeries[i] - timeSeries[i - 1]
            else:
                total_poison_time += duration
            i += 1
        total_poison_time += duration  # For the last attack
        return total_poison_time
