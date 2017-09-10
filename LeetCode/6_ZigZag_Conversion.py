class Solution(object):
    """
    Δ=2n-2    1                           2n-1                         4n-3
    Δ=        2                     2n-2  2n                    4n-4   4n-2
    Δ=        3               2n-3        2n+1              4n-5       .
    Δ=        .           .               .               .            .
    Δ=        .       n+2                 .           3n               .
    Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
    Δ=2n-2    n                           3n-2                         5n-4
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows_with_char = [[] for _ in range(numRows)]
        is_zigzag_order = False  # Initially, it's false
        cur_index = 0

        for i in xrange(len(s)):
            if is_zigzag_order:
                rows_with_char[cur_index].append(s[i])
                if numRows + cur_index == 0:
                    is_zigzag_order = False
                    cur_index = 1
                else:
                    cur_index -= 1
            else:
                rows_with_char[cur_index].append(s[i])
                cur_index += 1
                if cur_index == numRows:
                    is_zigzag_order = True
                    cur_index = -2

        new_str = ""
        for each_row in range(numRows):
            new_str += "".join(rows_with_char[each_row])
        return new_str

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
