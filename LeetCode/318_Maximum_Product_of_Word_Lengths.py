# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # For each word, find its unshared word set
        words_bitmap = []
        for each in words:
            cur_bitmap = 0
            for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
                if c in each:
                    cur_bitmap |= 1 << i
            words_bitmap.append(cur_bitmap)
        max_len_prod = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words_bitmap[i] & words_bitmap[j] == 0:
                    max_len_prod = max(max_len_prod, len(words[i]) * len(words[j]))

        return max_len_prod
