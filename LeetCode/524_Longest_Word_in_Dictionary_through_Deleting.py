# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # Find longest subsequence in the dict
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""


s = Solution()
input_s = "bab"
d = ["ba","ab","a","b"]
# d = ["ale","apple","monkey","plea"]
print(s.findLongestWord(input_s, d))





