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

s = Solution()
print(s.canIWin(5, 50))


