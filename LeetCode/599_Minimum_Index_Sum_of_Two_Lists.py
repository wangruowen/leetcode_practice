# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        interest_map = {}
        for i, c in enumerate(list1):
            interest_map[c] = [i]
        for j, c in enumerate(list2):
            if c in interest_map:
                interest_map[c].append(j)

        index_sum = len(list1) + len(list2)
        result = []
        for each in interest_map:
            value = interest_map[each]
            if len(value) > 1:
                if index_sum > sum(value):
                    index_sum = sum(value)
                    result = [each]
                elif index_sum == sum(value):
                    result.append(each)
        return result
