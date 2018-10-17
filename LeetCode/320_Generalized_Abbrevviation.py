# http://www.cnblogs.com/grandyang/p/5261569.html
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # Given the rest of the word, we can either change the first letter to 1
        # or keep it and continue with the rest
        result = []

        def helper(prefix_before_num, abbr_num, remain_word):
            nonlocal result
            if len(remain_word) == 0:
                if abbr_num > 0:
                    prefix_before_num += str(abbr_num)
                result.append(prefix_before_num)
                return

            # Two cases,
            # 1. Change cur letter to 1
            helper(prefix_before_num, abbr_num + 1, remain_word[1:])

            # 2. Keep current letter
            if abbr_num > 0:
                prefix_before_num += str(abbr_num)
            helper(prefix_before_num + remain_word[0], 0, remain_word[1:])
        helper("", 0, word)

        return result

s = Solution()
word = "word"
print(s.generateAbbreviations(word))