# https://leetcode.com/problems/jewels-and-stones
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_hashmap = {}
        for j in J:
            jewel_hashmap[j] = 0
        for s in S:
            if s in jewel_hashmap:
                jewel_hashmap[s] += 1

        sum = 0
        for j in J:
            sum += jewel_hashmap[j]

        return sum
    """
    setJ = set(J)
        return sum(s in setJ for s in S)
    """
