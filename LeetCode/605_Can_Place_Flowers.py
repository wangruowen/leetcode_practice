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

    def canPlaceFlowers_v2(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Two pointers
        result = 0
        cur_1, next_1 = -2, 0
        while next_1 < len(flowerbed) and flowerbed[next_1] != 1:
            next_1 += 1
        if next_1 == len(flowerbed):
            next_1 += 1  # Make next_1 super large if it already reaches the end

        for i, c in enumerate(flowerbed):
            need_update = False
            if c == 1:
                need_update = True
            elif cur_1 + 1 < i < next_1 - 1:
                result += 1
                need_update = True

            if need_update:
                cur_1 = i
                if i + 1 >= next_1:
                    next_1 += 1
                    while next_1 < len(flowerbed) and flowerbed[next_1] != 1:
                        next_1 += 1
                    if next_1 == len(flowerbed):
                        next_1 += 1  # Make next_1 super large if it reaches the end
        return result >= n

s = Solution()
# flowerbed = [0,0,1,0,0]
flowerbed = [1,0,0,0,0,1]
n = 2
print(s.canPlaceFlowers_v2(flowerbed, n))

