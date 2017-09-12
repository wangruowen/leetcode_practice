class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        Brute Force
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        cur_s2_index = 0
        repeat_count = 0
        for i in range(n1):
            for c in s1:
                if c == s2[cur_s2_index]:
                    cur_s2_index += 1
                if cur_s2_index == len(s2):
                    repeat_count += 1
                    cur_s2_index = 0

        return repeat_count / n2

s = Solution()
s1 = "lovenicoloveliveniconiconiconiniconjcoaaajo"
n1 = 201641
s2 = "lovenanjo"
n2 = 401

print(s.getMaxRepetitions(s1, n1, s2, n2))
