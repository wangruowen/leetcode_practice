# https://leetcode.com/problems/swap-adjacent-in-lr-string/
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        # As long as "R" has "X" on its right side, "R" can shift to right until hit "L"
        # Same, if "L" has "X" on its left side, "L" can shift to left until hit "R"
        # So, "R" can shift to right within the range to the next "L"
        # "L" can shift to left within the range to the prev "R"
        # In other words, imagine "L" and "R" can only move within the range of prev/next "R" and "L"
        s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
        if len(s) != len(e):
            return False
        for (c_s, i_s), (c_e, i_e) in zip(s, e):
            if c_s != c_e:
                return False
            if c_s == 'L' and i_s < i_e:
                # we can only move left, if we found it move right, wrong
                return False
            if c_s == 'R' and i_s > i_e:
                return False
        return True


s = Solution()
# start = "RXXLRXRXL"
# end = "XRLXXRRLX"
start = "X"
end = "L"
print(s.canTransform(start, end))

