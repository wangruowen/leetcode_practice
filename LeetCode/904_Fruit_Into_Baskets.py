# https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # Problem
        #
        # "Start from any index, we can collect at most two types of fruits. What is the maximum amount"
        #
        # Translation
        #
        # Find out the longest length of subarrays with at most 2 different numbers?
        start = 0
        types = {}
        max_len = 0
        for i, c in enumerate(tree):
            types[c] = types.get(c, 0) + 1

            while start < i and len(types) > 2:
                types[tree[start]] -= 1
                if types[tree[start]] == 0:
                    del types[tree[start]]
                start += 1

            max_len = max(max_len, i - start + 1)

        return max_len


s = Solution()
tree = [0, 1, 2, 2]
print(s.totalFruit(tree))
