# https://leetcode.com/problems/additive-number/description/
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # The goal is to find the first num and recursively call the rest
        def helper(prev, num):
            for i in range(1, len(num)):
                if i > 1 and num[0] == '0':
                    break

                cur = int(num[:i])
                target = prev + cur
                len_target = len(str(target))
                if i + len_target > len(num):
                    return False
                elif num[i:i+len_target] == str(target):
                    if i + len_target == len(num) or helper(cur, num[i:]):
                        return True

            return False

        for j in range(1, len(num)):
            if j > 1 and num[0] == '0':
                break

            if helper(int(num[:j]), num[j:]):
                return True
        return False

s = Solution()
print(s.isAdditiveNumber("101"))


