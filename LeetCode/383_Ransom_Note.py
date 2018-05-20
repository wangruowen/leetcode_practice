# https://leetcode.com/problems/ransom-note/description/
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note_map = {}
        for each in ransomNote:
            note_map[each] = note_map.get(each, 0) + 1
        for each in magazine:
            if each in note_map:
                note_map[each] -= 1
        for each in note_map:
            if note_map[each] > 0:
                return False
        return True
