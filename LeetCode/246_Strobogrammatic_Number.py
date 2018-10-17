# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number.py
class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        """Should be mirror symmetric"""
        for i in range(len(num) // 2):
            if num[i] not in self.lookup or self.lookup[num[i]] != num[-i - 1]:
                return False
        return True

s = Solution()
print(s.isStrobogrammatic("6108019"))
