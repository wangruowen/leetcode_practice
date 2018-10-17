from collections import Counter, defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = {}  # stats_bitmap_str -> List
        for each_str in strs:
            char_stats_key = Solution.get_char_stats(each_str)
            if char_stats_key in anagram_dict:
                anagram_dict[char_stats_key].append(each_str)
            else:
                anagram_dict[char_stats_key] = [each_str]
        return anagram_dict.values()

    @staticmethod
    def get_char_stats(each_str):
        stats_map = [0] * 26  # char_index -> num
        for c in each_str:
            i = ord(c) - ord('a')
            stats_map[i] += 1

        return "".join(map(lambda x: str(x), stats_map))

    def groupAnagrams_v2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = defaultdict(list)
        for each in strs:
            counter_str = []
            counter = Counter(each)
            for k in sorted(counter.keys()):
                counter_str.append(k + ":" + str(counter[k]))
            anagram_dict[",".join(counter_str)].append(each)

        return list(anagram_dict.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
