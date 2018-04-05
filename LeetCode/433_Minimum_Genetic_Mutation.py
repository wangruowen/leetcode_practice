# https://leetcode.com/problems/minimum-genetic-mutation/description/
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # This is similar to the Word Ladder one
        # BFS Search
        cur_layer_set = set([start])
        length = 0
        rest_bank = set(bank)

        while len(cur_layer_set) > 0 and len(rest_bank) > 0:
            length += 1
            next_layer_set = set()
            for each_gene in cur_layer_set:
                one_char_diff_set = self.get_one_char_diff_set(each_gene)
                valid_ones = one_char_diff_set.intersection(rest_bank)
                next_layer_set = next_layer_set.union(valid_ones)
                if end in next_layer_set:
                    return length

            cur_layer_set = next_layer_set
            rest_bank -= cur_layer_set

        return -1


    def get_one_char_diff_set(self, gene):
        result = set()
        for i in range(len(gene)):
            for c in "ACGT":
                if c == gene[i]: continue
                # replace gene[i] with c
                result.add(gene[:i] + c + gene[i + 1:])

        return result

s = Solution()



start = "AACCTTGG"
end = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
print(s.minMutation(start, end, bank))