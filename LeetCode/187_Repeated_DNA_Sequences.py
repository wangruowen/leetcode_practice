# https://leetcode.com/problems/repeated-dna-sequences/description/
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # A, C, G, T can be represented as 00, 01, 10, 11
        ACGT_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        pattern_map = {}
        pattern_counter = Counter()
        cur_subseq = 1  # put a leading 1, to make AAAAAAAAAA to be non-zero
        # Now 10-letter-long should be 21 bit, using mask 0x1fffff
        for i, c in enumerate(s):
            cur_subseq <<= 2
            cur_subseq &= 0xfffff
            cur_subseq |= ACGT_map[c]
            if i >= 9:
                cur_subseq |= 0x100000  # Keep leading 1 to avoid all 0
                pattern_counter[cur_subseq] += 1
                pattern_map[cur_subseq] = s[i - 9:i + 1]

        return [pattern_map[k] for k, v in pattern_counter.items() if v > 1]

s = Solution()
test_str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(s.findRepeatedDnaSequences(test_str))



