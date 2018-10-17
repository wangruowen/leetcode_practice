# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointers, one forward, one backward
        vowels = "aeiouAEIOU"
        s = list(s)  # str is immutable
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1
            while p1 < p2 and s[p2] not in vowels:
                p2 -= 1
            if p1 < p2:
                s[p1], s[p2] = s[p2], s[p1]
            else:
                break
            p1 += 1
            p2 -= 1

        return "".join(s)

s = Solution()
print(s.reverseVowels("aA"))