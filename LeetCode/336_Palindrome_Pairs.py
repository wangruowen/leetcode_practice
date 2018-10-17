# https://leetcode.com/problems/palindrome-pairs/description/
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 1. tab | bat, word == reversed(word)
        # 2. tabb + at => ta|bbat, reversed(word[:2]) == match_word and word[2:] == reversed(word[2:])
        # 3. bbat + at => at|bbat, reversed(word[2:]) == match_word and word[:2] == reversed(word[:2])
        lookup = {each: i for i, each in enumerate(words)}
        result = set()
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                first_part, second_part = words[i][:j], words[i][j:]
                if first_part[::-1] in lookup and second_part == second_part[::-1] and lookup[first_part[::-1]] != i:
                    result.add((i, lookup[first_part[::-1]]))
                if first_part == first_part[::-1] and second_part[::-1] in lookup and lookup[second_part[::-1]] != i:
                    result.add((lookup[second_part[::-1]], i))

        return [list(each) for each in result]



