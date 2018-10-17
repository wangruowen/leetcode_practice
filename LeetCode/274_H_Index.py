# https://leetcode.com/problems/h-index/description/
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # for i-th item in h_array keeps how many papers have i citations
        h_array = [0 for _ in range(len(citations) + 1)]
        for each in citations:
            if each >= len(citations):
                h_array[len(citations)] += 1
            else:
                h_array[each] += 1

        # Then we count how many papers have >= i citations in reverse order
        total_papers = 0
        for i in range(len(citations), -1, -1):
            total_papers += h_array[i]
            if total_papers >= i:
                return i

        return 0

s = Solution()
cit = [1,1]
print(s.hIndex(cit))