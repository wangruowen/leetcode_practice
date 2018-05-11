# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for each in letters:
            if ord(target) < ord(each):
                return each
        return letters[0]

    def nextGreatestLetter_v2(self, letters, target):
        # version 2
        import bisect
        pos = bisect.bisect_right(letters, target)
        return letters[pos] if pos != len(letters) else letters[0]
