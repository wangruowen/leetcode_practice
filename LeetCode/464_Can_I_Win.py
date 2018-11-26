# https://leetcode.com/problems/can-i-win/description/
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # Corner case
        avail_nums = list(range(1, maxChoosableInteger + 1))
        if sum(avail_nums) < desiredTotal:
            return False
        # minimax
        self.mem = {}
        return self.helper(avail_nums, desiredTotal)


    def helper(self, avail_nums, restToTotal):
        # prepare bitmap for DP memorize
        bitmap_avail_nums = 0
        for i in avail_nums:
            bitmap_avail_nums |= 1 << i
        key = "%d %d" % (bitmap_avail_nums, restToTotal)

        if key not in self.mem:
            # We just try each number and recursively do this to
            # find out the max chance we have
            for i in range(len(avail_nums)):
                cur = avail_nums[i]
                if cur >= restToTotal:
                    self.mem[key] = True
                    return True

                new_nums = avail_nums[:i] + avail_nums[i+1:]
                # If the other play return False, we get True
                if not self.helper(new_nums, restToTotal - cur):
                    self.mem[key] = True
                    return True
            self.mem[key] = False

        return self.mem[key]

    def canIWin_v2(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal == 0:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        dp_cache = {}  # Key is (remain_nums_bitmap, sum_so_far)

        def to_bitmap(remain_nums):
            bitmap = 0
            for i in remain_nums:
                bitmap |= 1 << i
            return bitmap

        def helper(remain_nums, sum_so_far=0):
            nonlocal dp_cache

            key = (to_bitmap(remain_nums), sum_so_far)
            if key in dp_cache:
                return dp_cache[key]

            if sum_so_far >= desiredTotal:
                dp_cache[key] = False
                return False

            for c in remain_nums:
                # print("Player ", player, " choose ", c)
                remain_nums.remove(c)
                if not helper(set(remain_nums), sum_so_far + c):
                    # If the other side has no way to win, then I win
                    dp_cache[key] = True
                    return True
                remain_nums.add(c)

            dp_cache[key] = False
            return False
        return helper(set(range(1, maxChoosableInteger + 1)))


s = Solution()
print(s.canIWin_v2(18,171))


