# https://leetcode.com/problems/text-justification/description/
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def construct_oneline(start, end, words_length):
            """
            Construct one line from index start to end (exclusive)
            :param start:
            :param end:
            :return:
            """
            oneline = ""
            space_length = maxWidth - words_length
            space_gaps = end - start - 1
            if space_gaps > 0:
                each_space = space_length // (end - start - 1) # space gaps are one less than words
                extra_spaces = space_length % (end - start - 1)
            else:
                each_space = space_length
                extra_spaces = 0
            for i in range(start, end):
                oneline += words[i]
                if i < end - 1 or space_gaps == 0:
                    oneline += " " * each_space
                    if extra_spaces > 0:
                        oneline += " "
                        extra_spaces -= 1
            return oneline

        start, length = 0, 0
        result = []
        for i, w in enumerate(words):
            cur_length = length + len(w) + (i - start) # Num of spaces from start to i
            if cur_length > maxWidth:
                result.append(construct_oneline(start, i, length))
                start, length = i, 0
            length += len(w)

        lastline = ""
        for k in range(start, len(words)):
            lastline += words[k]
            if k < len(words) - 1:
                lastline += " "
        lastline += " " * (maxWidth - len(lastline))  # padding spaces
        result.append(lastline)

        return result

s = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
for each in s.fullJustify(words, maxWidth):
    print(each)

