# https://leetcode.com/problems/remove-invalid-parentheses/
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def findMinRemove(s):
            """
            Return the number of left open parentheses and right close parentheses
            that have to be removed
            :param s:
            :return:
            """
            open_paren, close2remove = 0, 0
            for c in s:
                if c == '(':
                    open_paren += 1
                elif c == ')':
                    if open_paren > 0:
                        open_paren -= 1
                    else:
                        # No open_paren can be matched, must remove
                        close2remove += 1

            # Note that we may have remaining open_paren that are not closed
            # which should also be removed
            return open_paren, close2remove

        def check_valid(s):
            open_paren = 0
            for c in s:
                if c == '(':
                    open_paren += 1
                elif c == ')':
                    open_paren -= 1
                    if open_paren < 0:
                        return False
            return open_paren == 0

        def DFS(i, open2remove, close2remove, new_s):
            """
            For s[i:], we need to remove open2remove and close2remove num of open and close parentheses.
            :param i:
            :param open2remove:
            :param close2remove:
            :return:
            """
            nonlocal result

            if i == len(s):
                if open2remove == close2remove == 0 and check_valid(new_s):
                    result.add(new_s)
                return

            if s[i] == '(':
                if open2remove > 0:
                    DFS(i + 1, open2remove - 1, close2remove, new_s)
            elif s[i] == ')':
                if close2remove > 0:
                    DFS(i + 1, open2remove, close2remove - 1, new_s)

            # And we can do nothing, add current letter and continue on the next letter
            DFS(i + 1, open2remove, close2remove, new_s + s[i])

        open2remove, clsoe2remove = findMinRemove(s)
        result = set()
        DFS(0, open2remove, clsoe2remove, "")
        return list(result)


s = Solution()
test = "()())()"
print(s.removeInvalidParentheses(test))