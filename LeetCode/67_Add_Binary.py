# https://leetcode.com/problems/add-binary/description/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = 1, 1
        while i <= len(a) and j <= len(b):
            cur = carry + int(a[-i]) + int(b[-j])
            if cur >= 2:
                result.append(str(cur - 2))
                carry = 1
            else:
                result.append(str(cur))
                carry = 0
            i += 1
            j += 1
        while i <= len(a):
            cur = carry + int(a[-i])
            if cur >= 2:
                result.append(str(cur - 2))
                carry = 1
            else:
                result.append(str(cur))
                carry = 0
            i += 1
        while j <= len(b):
            cur = carry + int(b[-j])
            if cur >= 2:
                result.append(str(cur - 2))
                carry = 1
            else:
                result.append(str(cur))
                carry = 0
            j += 1
        if carry == 1:
            result.append(str(carry))
        return "".join(reversed(result))

a = "11"
b = "1"
s = Solution()
print(s.addBinary(a, b))

