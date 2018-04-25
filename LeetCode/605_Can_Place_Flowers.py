# https://leetcode.com/problems/can-place-flowers/description/
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        one_indices = [i for i in xrange(len(flowerbed)) if flowerbed[i] == 1]
        prev_one_index = -1
        k = 0
        next_one_index = one_indices[k] if k < len(one_indices) else -1
        k += 1
        plottable_count = 0
        for i in xrange(len(flowerbed)):
            if i == next_one_index:
                prev_one_index = next_one_index
                next_one_index = one_indices[k] if k < len(one_indices) else -1
                k += 1
            else:
                if (prev_one_index == -1 or abs(i - prev_one_index) > 1)\
                        and (next_one_index == -1 or abs(i - next_one_index) > 1):
                    plottable_count += 1
                    prev_one_index = i  # mark current i as new one

        return plottable_count >= n

s = Solution()
flowerbed = [0,0,1,0,0]
n = 1
print(s.canPlaceFlowers(flowerbed, n))

