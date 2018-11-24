# https://leetcode.com/problems/strobogrammatic-number-ii/
class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Strobogrammatic number is like Palindrome String
        # The first and last digit should match each other
        # If n is odd, the middle digit has to be 0, 1, 8
        stro_digits = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        if n == 1:
            return ['0', '1', '8']

        def DFS(i):
            """
            Change i-th digit in the number
            :param num:
            :param i:
            :return:
            """
            result = []
            if i == 0:
                candidates = "1689"
            elif 0 < i < n // 2:
                candidates = "01689"
            elif i == n // 2:
                if n % 2 == 1:
                    return ["0", "1", "8"]
                else:
                    # if n is even, n // 2 is already the later half
                    return [""]

            for d in candidates:
                prefix, suffix = d, stro_digits[d]
                for each in DFS(i + 1):
                    result.append(prefix + each + suffix)
            return result

        return DFS(0)

s = Solution()
print(s.findStrobogrammatic(1))
