class Solution(object):
    def __init__(self):
        self.digit_char_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_comb = []
        if len(digits) < 1:
            return []

        if len(digits) == 1:
            char_comb = [c for c in self.digit_char_map[int(digits)]]
        else:
            cur_chars = self.digit_char_map[int(digits[0])]
            sub_comb = self.letterCombinations(digits[1:])
            for each_char in cur_chars:
                char_comb.extend([each_char + each_sub_comb for each_sub_comb in sub_comb])
        return char_comb

s = Solution()
print(s.letterCombinations("23"))
