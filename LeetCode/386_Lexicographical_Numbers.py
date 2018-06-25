# https://leetcode.com/problems/lexicographical-numbers/description/
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # The idea is a dynamic generator to find the next num to add
        # If cur is 19, next check 190, 1900, 2, 20
        result = []
        cur = 1
        # iterate n - 1 times, because we already append first 1
        for _ in range(n):
            # print(cur)
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            elif cur % 10 != 9 and cur + 1 <= n:
                cur += 1
            elif cur % 10 == 9:
                # e.g., 19 -> 2, 199 -> 2
                cur = (cur + 1) // 10
                while cur % 10 == 0:
                    cur //= 10
            else:
                # e.g., 13 -> 2 if 13 is n
                cur = cur // 10 + 1
                while cur % 10 == 0:
                    cur //= 10
        return result


s = Solution()
print(s.lexicalOrder(13))