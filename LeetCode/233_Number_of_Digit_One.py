# https://leetcode.com/problems/number-of-digit-one/
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Basic idea: count number of combination of 1 at each digit in two cases: prefix appears or not
        # Eg.3101592:
        # 1) one at hundreds:      1 (< 5): [1~3101]1[0~99]. So # = 3101 * 100 + 100 (Safe since 31011XX never be greater than 31015XX)
        # 2) one at thousands:     1 (= 1): [1~310]1[0~592]. So # = 310 * 1000 + (592 + 1) (Unsafe if prefix is 0, it must be <= 1592)
        # 3) one at ten thousands: 1 (> 0): [1~30]1[0~9999]. So # = 30 * 10000 (If prefix is 0, no 1 digit number exist)
        # 4) one at tens:   1 (< 9): [1-31015]1[0-9]. So # = 31015 * 10
        if n <= 0: return 0
        ones = 0
        i, q = 1, n
        while i <= n:
            prefix, cur, surfix = n // (i * 10), q % 10, n % i
            ones += prefix * i
            if cur > 1:
                ones += i
            elif cur == 1:
                ones += surfix + 1  # plus 0
            i *= 10
            q //= 10
        return ones

