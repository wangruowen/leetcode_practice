# https://leetcode.com/problems/most-common-word/description/
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_count = {}
        for each in map(lambda x: x.lower(), paragraph.split()):
            if each[-1] in "!?',;.":
                each = each[:-1]
            if each in banned:
                continue
            else:
                word_count[each] = word_count.get(each, 0) + 1

        max_count = 0
        max_word = None
        for each in word_count:
            if word_count[each] > max_count:
                max_count = word_count[each]
                max_word = each
        return max_word