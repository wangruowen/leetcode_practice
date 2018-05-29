# https://leetcode.com/problems/pyramid-transition-matrix/description/
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # Backtracking
        if len(bottom) == 1:
            return True
        upper_layer = [""]
        for i in range(len(bottom) - 1):
            one_pair = bottom[i:i + 2]
            candidates = []
            for each in allowed:
                if one_pair == each[:2]:
                    candidates.append(each[2])
            if len(candidates) == 0:
                return False
            tmp_upper_layer = []
            for each_so_far in upper_layer:
                for each_cand in candidates:
                    tmp_upper_layer.append(each_so_far + each_cand)
            upper_layer = tmp_upper_layer

        for each_upper_layer in upper_layer:
            if self.pyramidTransition(each_upper_layer, allowed):
                return True
        return False

s = Solution()
bottom = "ABC"
allowed = ["ABD","BCE","DEF","FFF"]
print(s.pyramidTransition(bottom, allowed))