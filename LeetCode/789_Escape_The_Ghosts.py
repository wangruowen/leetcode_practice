# https://leetcode.com/problems/escape-the-ghosts/description/
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # https://leetcode.com/problems/escape-the-ghosts/discuss/116678/Why-interception-in-the-middle-is-not-a-good-idea-for-ghosts.
        # Based on the above analysis, we just need to calculate the distances between
        # our pacman and the target, and the distances between ghost and target and compare
        # Note that the distance is calculated in Manhattan style
        pacman_dist = abs(target[0]) + abs(target[1])
        for ghost_x, ghost_y in ghosts:
            ghost_dist = abs(target[0] - ghost_x) + abs(target[1] - ghost_y)
            if ghost_dist <= pacman_dist:
                return False
        return True

