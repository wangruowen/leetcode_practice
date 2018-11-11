# http://www.cnblogs.com/grandyang/p/8970057.html
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # Find K-th Smallest Pair Distance
        #
        # Kth Smallest Number in Multiplication Table
        #
        # Maximum Average Subarray II
        #
        # Kth Smallest Element in a Sorted Matrix
        
        left, right = 0, 10**8
        # guess mid value to be the max distance between any two
        # And keep trying mid values to see if we can match K
        def count_stations(dist):
            count = 0
            for i in range(len(stations) - 1):
                # we need to add the following number of new stations in between
                count += int((stations[i + 1] - stations[i]) / mid)
            return count

        while right - left > 1e-6:
            mid = (left + right) / 2
            if count_stations(mid) <= K:
                right = mid
            else:
                left = mid
        return left


