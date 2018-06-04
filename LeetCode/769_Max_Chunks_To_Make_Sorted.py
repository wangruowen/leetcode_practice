# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # In order to be sorted after concatenating,
        # the chunks's position should be the same of sorted array
        chunk_count = 0
        i = 0
        max_pos = -1
        while i < len(arr):
            if i < arr[i]:
                # arr[i] refers to a bigger index
                max_pos = max(max_pos, arr[i])
            elif max_pos > i:
                # max_pos > i >= arr[i]:
                pass
            elif max_pos == i:
                # Previous chunk can be finished at this point
                max_pos = -1
                chunk_count += 1
            elif i == arr[i]:
                chunk_count += 1
            i += 1

        return chunk_count

    def clean_version(self, arr):
        chunks = 0
        max_see = 0
        for i, c in enumerate(arr):
            max_see = max(max_see, c)
            if max_see == i:
                chunks += 1
        return chunks

s = Solution()
# arr = [4,3,2,1,0]
# arr = [1,2,3,4,5,0]
# arr = [1,0,2,3,4]
arr = [5,4,7,6,8]
print(s.maxChunksToSorted(arr))