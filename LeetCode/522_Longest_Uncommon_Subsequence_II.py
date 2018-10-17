# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
from collections import defaultdict

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # The idea is to find the longest str, which is not a subsequence of each other str
        max_len = -1
        len_map = defaultdict(int)
        strs.sort(key=lambda x: len(x))
        print(strs)

        last_str = None
        for cur_str in strs:
            len_map[cur_str] += 1
            if last_str == cur_str:
                continue

            for each_exist in len_map:
                if each_exist != cur_str and self.is_subsequence(each_exist, cur_str):
                    len_map[each_exist] = -1

            last_str = cur_str
        for each in len_map:
            if len_map[each] == 1:
                max_len = max(max_len, len(each))

        return max_len

    def is_subsequence(self, exist, cur):
        """
        Return exist str is a subsequence of the cur str
        :param exist:
        :param cur:
        :return:
        """
        i, j = 0, 0
        while i < len(exist) and j < len(cur):
            if exist[i] == cur[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(exist)


s = Solution()
a = ["aabbcc", "aabbcc","c","e","aabbcd"]
print(s.is_subsequence("abc", "aabbcc"))
print(s.findLUSlength(a))
