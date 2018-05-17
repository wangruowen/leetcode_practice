# https://leetcode.com/problems/add-strings/description/
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            if i >= 0:
                val_i = num1[i]
                i -= 1
            else:
                val_i = '0'
            if j >= 0:
                val_j = num2[j]
                j -= 1
            else:
                val_j = '0'
            cur = carry + ord(val_i) - ord('0') + ord(val_j) - ord('0')
            if cur >= 10:
                cur -= 10
                carry = 1
            else:
                carry = 0
            result.insert(0, chr(cur + ord('0')))

        if carry == 1:
            result.insert(0, chr(carry + ord('0')))
        return "".join(result)

s = Solution()
num1, num2 = "123", "4567"
print(s.addStrings(num1, num2))
