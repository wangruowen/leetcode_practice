# https://leetcode.com/problems/rectangle-area/#/description

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1, S2 = (C - A) * (D - B), (G - E) * (H - F)
        if C <= E or A >= G or B >= H or D <= F:
            # No overlap
            return S1 + S2
        else:
            return S1 + S2 - self.find_shared_area(A, B, C, D, E, F, G, H)


    def find_shared_area(self, A, B, C, D, E, F, G, H):
        if C <= E or A >= G or B >= H or D <= F:
            # No overlap
            return 0

        # Then find the overlap
        if A <= E:
            overlap_left_x = E
        else:
            overlap_left_x = A
        if C >= G:
            overlap_right_x = G
        else:
            overlap_right_x = C
        if B <= F:
            overlap_down_y = F
        else:
            overlap_down_y = B
        if D >= H:
            overlap_up_y = H
        else:
            overlap_up_y = D

        # Calculate the size
        return (overlap_right_x - overlap_left_x) * (overlap_up_y - overlap_down_y)

    def computeArea_v2(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # Just sum two rectangles and minus the possible dup area
        two_rec_sum = (D-B) * (C-A) + (H-F) * (G-E)
        # For dup area
        dup_down_left = [max(A, E), max(B, F)]
        dup_up_right = [min(C, G), min(D, H)]
        # It is possible that dup_up_right is smaller than dup_down_left, in which case, there is no overlap
        dup_area = max(0, dup_up_right[0] - dup_down_left[0]) * max(0, dup_up_right[1] - dup_down_left[1])
        return two_rec_sum - dup_area