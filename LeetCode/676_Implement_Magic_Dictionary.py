# https://leetcode.com/problems/implement-magic-dictionary/description/
from collections import defaultdict

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len2word = {}
        # {len: {each_word: one_char_diff_set}}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for each in dict:
            if len(each) not in self.len2word:
                self.len2word[len(each)] = {}
            cur_set = set()
            for i in range(len(each)):
                cur_set.add(each[:i] + "_" + each[i + 1:])
            self.len2word[len(each)][each] = cur_set

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.len2word:
            return False

        cur_word_len_dict = self.len2word[len(word)]
        modify_word_set = set()
        for i in range(len(word)):
            modify_word_set.add(word[:i] + "_" + word[i + 1:])

        for each_word in cur_word_len_dict:
            if word == each_word:
                continue
            if len(modify_word_set.intersection(cur_word_len_dict[each_word])) > 0:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)