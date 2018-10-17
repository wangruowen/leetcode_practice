# https://leetcode.com/problems/hand-of-straights/description/
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        len_hand = len(hand)
        if len_hand < W or len_hand % W != 0:
            print("len_hand % W != 0")
            return False
        hand.sort()

        # DFS
        def DFS(i, group_size, v):
            v.add(i)
            if group_size == W:
                return True

            j = i + 1
            while j < len_hand:
                if j not in v and hand[j] == hand[i] + 1:
                    return DFS(j, group_size + 1, v)
                j += 1
            return False

        i = 0
        visited = set()
        while i < len_hand:
            if i not in visited:
                if not DFS(i, 1, visited):
                    return False
            i += 1

        return len(visited) == len_hand

s = Solution()
hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(s.isNStraightHand(hand, W))

