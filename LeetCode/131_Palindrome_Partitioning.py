# https://leetcode.com/problems/palindrome-partitioning/description/
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Backtracking
        if len(s) == 0:
            return [[""]]
        result = []
        self._helper(s, [], result)
        return result

    def _helper(self, s, parti_so_far, result):
        if len(s) == 0:
            result.append(parti_so_far[:])
            return

        for i in range(1, len(s) + 1):
            cur_str = s[:i]
            if cur_str == cur_str[::-1]:
                parti_so_far.append(s[:i])
                self._helper(s[i:], parti_so_far, result)
                parti_so_far.pop()

    def partition_v2(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def helper(i, stack):
            if i == len(s):
                result.append(stack[:])
                return

            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    stack.append(s[i:j])
                    helper(j, stack)
                    stack.pop()

        helper(0, [])
        return result
s = Solution()
a = "aab"
print(s.partition(a))