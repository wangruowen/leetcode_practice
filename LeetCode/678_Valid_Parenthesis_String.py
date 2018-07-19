# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString_recursive(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Recursive, has TLE issue
        def helper(left_par, s):
            for i, c in enumerate(s):
                if c == "(":
                    left_par += 1
                elif c == ")":
                    if left_par == 0:
                        return False
                    left_par -= 1
                else:
                    # 1. Treat as ( or )
                    if helper(left_par + 1, s[i+1:]):
                        return True
                    if left_par > 0 and helper(left_par - 1, s[i+1:]):
                        return True
                    # 2. Treat as empty
            return left_par == 0
        return helper(0, s)

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Greedy, Since '*' can be treated as empty or either open parenthesis or close parenthesis, this becomes a range
        min_left, max_left = 0, 0
        # as long as c != "(", we treat ")" or "*" as ")", min_left -= 1
        # as long as c != ")", we treat "(" or "*" as "(", max_left += 1
        # In the end, if min_left > 0, which means all "*" have been treated as ")" but still have more "(", then False
        #             if max_left < 0, which means all "*" have been treated as "(" but still have more ")", then False
        for c in s:
            if c != "(":
                if min_left > 0:
                    min_left -= 1
            else:
                min_left += 1
            if c != ")":
                max_left += 1
            else:
                max_left -= 1
                if max_left < 0:
                    return False

        return min_left == 0



s = Solution()
# print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))