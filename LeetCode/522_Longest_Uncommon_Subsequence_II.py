# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_len = -1
        len_map = {}
        strs.sort(key=lambda x: len(x))
        print(strs)

        last_str = None
        for cur_str in strs:
            if last_str == cur_str:
                len_map[cur_str] = 2
                continue

            for each_exist in len_map:
                if self.is_subsequence(each_exist, cur_str):
                    len_map[each_exist] = -1

            len_map[cur_str] = len_map.get(cur_str, 0) + 1

            last_str = cur_str
        for each in len_map:
            if len_map[each] == 1:
                max_len = max(max_len, len(each))

        return max_len

    def is_subsequence(self, exist, cur):
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
