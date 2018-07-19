# https://github.com/kamyu104/LeetCode/blob/master/Python/next-closest-time.py
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Just loop one day, 24 hour, 1440 minutes, if the new time digits can be formed by the digits
        HH, MM = time.split(":")
        digit_strs = set([d for i in time.split(":") for d in i])
        cur_time = 60 * int(HH) + int(MM)

        # Now let's loop 1440 minutes
        for _ in range(1440):
            cur_time += 1
            cur_time %= 1440
            HH, MM = "%02d" % (cur_time // 60), "%02d" % (cur_time % 60)
            cur_digits = set(list(HH) + list(MM))
            if cur_digits.issubset(digit_strs):
                return HH + ":" + MM




