# https://leetcode.com/problems/word-pattern/description/
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False

        pattern2word, word2pattern = {}, {}
        for i in range(len(words)):
            cur_p2w, cur_w2p = None, None
            if pattern[i] in pattern2word:
                cur_p2w = pattern2word[pattern[i]]
            if words[i] in word2pattern:
                cur_w2p = word2pattern[words[i]]
            if not cur_p2w and not cur_w2p:
                pattern2word[pattern[i]] = words[i]
                word2pattern[words[i]] = pattern[i]
            elif cur_w2p != pattern[i] or cur_p2w != words[i]:
                return False

        return True
