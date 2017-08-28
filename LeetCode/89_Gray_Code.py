class Solution(object):
    def grayCode(self, n):
        """
            00
            01
            11
            10
          ---- Mirror Back
           110
           111
           101
           100
          ----
          1100
          1101
          1111
          1110
          1010
          1011
          1001
          1000
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        last_result = []
        for i in range(n):
            if i == 0:
                last_result = [0b0, 0b1]
            else:
                tmp_list = []
                leading_one = 0b1 << i
                for j in range(1, 2 ** i + 1):
                    tmp_list.append(leading_one | last_result[-j])
                last_result.extend(tmp_list)

        return last_result


s = Solution()
print(map(lambda x: bin(x), s.grayCode(4)))
