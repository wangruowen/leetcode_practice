# https://leetcode.com/problems/shortest-completing-word/description/
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()
        letter_map = {c: licensePlate.count(c) for c in licensePlate if c.isalpha()}
        len_result = 2**32 -1
        for each in words:
            each_lower = each.lower()
            found = True
            for c in letter_map:
                if c not in each_lower or letter_map[c] > each_lower.count(c):
                    found = False
            if found:
                if len(each) < len_result:
                    len_result = len(each)
                    result = each

        return result

    def shortestCompletingWord_v2(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        min_len, min_len_word = float('inf'), None
        plate_counter = Counter(licensePlate.lower())
        for each in words:
            word_counter = Counter(each.lower())
            found = True
            for k, v in plate_counter.items():
                if k.isalpha() and word_counter[k] < v:
                    found = False
                    break
            if found and min_len > len(each):
                min_len = len(each)
                min_len_word = each

        return min_len_word