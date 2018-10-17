# https://leetcode.com/problems/h-index-ii/description/
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(n)
        # for i, c in enumerate(citations):
        #     num_from_cur = len(citations) - i
        #     if num_from_cur <= c:
        #         return num_from_cur
        # return 0

        # Binary Search O(logn)
        l, r = 0, len(citations)
        while l < r:
            mid = (l + r) // 2
            h = len(citations) - mid
            if citations[mid] >= h:
                r = mid
            else:
                l = mid + 1
        return len(citations) - l

s = Solution()
citations = [0, 1, 3, 5, 6]
print(s.hIndex(citations))