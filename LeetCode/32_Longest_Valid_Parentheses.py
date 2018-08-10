# https://leetcode.com/problems/longest-valid-parentheses/description/
class Solution:
    def longestValidParentheses_old(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Every time, we encounter a '(', all previous matched pairs are pending on this one
        # Count number of matched pairs within every nested (), and gradually sum up together
        stack, len_stack = [], []
        max_len = 0
        for c in s:
            if c == '(':
                stack.append(c)
                len_stack.append('|')
            elif len(stack) > 0 and stack[-1] == '(':
                stack.pop()
                tmp = 2
                while len(len_stack) > 0 and len_stack[-1] != '|':
                    tmp += len_stack.pop()
                if len_stack[-1] == '|':
                    len_stack.pop()
                len_stack.append(tmp)
            else:
                len_stack.append('|')

        cur_len = 0
        for each in len_stack:
            if each == '|':
                max_len = max(max_len, cur_len)
                cur_len = 0
            else:
                cur_len += each

        return max(max_len, cur_len)

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Keep index, and use index to calculate the longest valid one
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)

        return max_len



s = Solution()
S = ")()())()()("
print(s.longestValidParentheses(S))
