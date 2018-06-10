# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
import heapq

class Solution(object):
    def __init__(self):
        self._dp = {}  # Each item is a list of (pair_sum, pair)

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Same as 378 Matrix, nums1, nums2 should form a matrix
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)


s = Solution()
nums1 = \
[-476570184,-423568801,-385585840,-375390924,-364630569,-359795128,-281872968,-126410430,-75677925,-54214495,-49178055,-32637211,-32198215,3413177,19045759,62248526,67551536,113606647,155411580,164755463,164781059,203133270,277305105,284913246,285973110,296436629,325431544,357294459,378678394,399786157]
print(len(nums1))
nums2 = \
[-408663357,-404578641,-376531700,-311642519,-294905976,-232001207,-183530032,-141524508,-115652480,-70696522,-63386299,-54656543,-32316999,29714175,33993996,45020708,62165363,84210823,93905151,102177224,209285622,288668099,328300713,338684779,342861859,384940859,408019604,410097843,458721542,475395296]
print(len(nums2))
k = 1000
print(s.kSmallestPairs(nums1, nums2, k))
