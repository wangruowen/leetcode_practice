# https://leetcode.com/problems/unique-morse-code-words/description/
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet_morse_table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                                "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                                "-.--", "--.."]
        all_transforms = set()
        for each_word in words:
            transform = ""
            for each_char in each_word:
                transform += alphabet_morse_table[ord(each_char) - ord('a')]
            all_transforms.add(transform)
        return len(all_transforms)
