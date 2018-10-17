# http://www.cnblogs.com/grandyang/p/5930369.html
class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, cur_count = 0, 0
        for c in abbr:
            if c.isalpha():
                if cur_count > 0:
                    i += cur_count
                    cur_count = 0

                if i >= len(word) or c != word[i]:
                    return False
                i += 1
            else:
                cur_count = 10 * cur_count + int(c)

        # remaining
        return i + cur_count == len(word)

s = Solution()
str1 = "internationalization"
abbr = "i12iz5"
# str1 = "apple"
# abbr = "a2e"
print(s.validWordAbbreviation(str1, abbr))