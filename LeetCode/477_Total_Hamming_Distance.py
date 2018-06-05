# https://leetcode.com/problems/total-hamming-distance/description/
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For all 32-bit integers, a given bit has many 0s and many 1s
        # each 0 and 1 pair is a difference. We need to count how many pairs
        # total distance for that bit is num(0) * num(1)
        total_hamming_dist = 0
        for i in range(32):
            mask = 1 << i
            one_count = 0
            for each in nums:
                if each & mask == mask:
                    one_count += 1
            total_hamming_dist += one_count * (len(nums) - one_count)
        return total_hamming_dist
