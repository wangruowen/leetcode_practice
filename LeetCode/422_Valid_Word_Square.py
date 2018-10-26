# http://www.cnblogs.com/grandyang/p/5991673.html
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if i >= len(words[j]) or j >= len(words) or words[i][j] != words[j][i]:
                    return False
        return True