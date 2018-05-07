# https://leetcode.com/problems/binary-watch/description/
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 4 digits for hours, 6 digits for minutes
        self.total_times = set()
        self.helper(num, 0, [])
        return list(self.total_times)

    def helper(self, n, start_index, bitmap):
        # two cases
        # 1. start_index bit is set
        # 2. start_index bit is unset
        if n == 0 or start_index == 10:
            # We are finished here:
            if n == 0:
                hour_str = "".join([str(x) for x in reversed(bitmap[:4])])
                hour = int(hour_str if len(hour_str) > 0 else "0", 2)
                if hour > 11:
                    return
                minute_str = "".join([str(x) for x in reversed(bitmap[4:])])
                minute = int(minute_str if len(minute_str) > 0 else "0", 2)
                if minute > 59:
                    return
                self.total_times.add("%d:%02d" % (hour, minute))
            return

        bitmap.append(1)
        self.helper(n - 1, start_index + 1, bitmap)
        bitmap.pop()
        bitmap.append(0)
        self.helper(n, start_index + 1, bitmap)
        bitmap.pop()

s = Solution()
print(s.readBinaryWatch(4))