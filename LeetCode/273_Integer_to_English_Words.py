# https://leetcode.com/problems/integer-to-english-words/description/
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        digit_name = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        units = ["", "Thousand", "Million", "Billion"]

        def parse_three_digits(three_digits):
            result = []
            if three_digits >= 100:
                result.append(digit_name[three_digits // 100])
                result.append("Hundred")
                three_digits %= 100
            if three_digits >= 20:
                result.append(digit_name[(three_digits // 10) * 10])
                if three_digits % 10 > 0:
                    result.append(digit_name[three_digits % 10])
            elif three_digits > 0:
                result.append((digit_name[three_digits]))
            return " ".join(result)

        result = []
        i = 0
        while num > 0:
            tmp_list = []
            low_three_digits = num % 1000
            if low_three_digits > 0:
                tmp_list.append(parse_three_digits(low_three_digits))
                if i > 0:
                    tmp_list.append(units[i])
            i += 1
            num //= 1000
            if len(tmp_list) > 0:
                result = tmp_list + result
        return " ".join(result)

s = Solution()
print(s.numberToWords(1234567891))