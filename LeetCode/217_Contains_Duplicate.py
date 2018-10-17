# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = set()
        for each in nums:
            if each in counter:
                return True
            else:
                counter.add(each)
        return False
