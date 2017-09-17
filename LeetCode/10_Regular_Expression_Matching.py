class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        use_dp = True
        if use_dp:
            return self.isMatch_v2(s, p, 0, 0)

        # if len(p) == 0:
        #     return len(s) == 0
        #
        # first_match = len(s) > 0 and p[0] in [s[0], "."]
        # if len(p) >= 2 and p[1] == "*":
        #     # 1. We keep the first match and continue to the next char in s, using current p
        #     # Note that, if first_match is False, python will short cut and directly assign False to the following
        #     # match_result_ignore_first_match = first_match and self.isMatch(s[1:], p)
        #
        #     # 2. Or we ignore the wildcard regex in p, and we start matching the same string using next regex in p
        #     # match_result_keep_first_match = self.isMatch(s, p[2:])
        #     return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_v2(self, s, p, i, j, memo={}):
        # check if s[i:] can be matched with p[j:]
        i_j_pair = (i, j)
        if i_j_pair not in memo:
            if j == len(p):
                match_result = i == len(s)
            else:
                first_match = i < len(s) and p[j] in [s[i], "."]
                if j < len(p) - 1 and p[j + 1] == "*":
                    match_result = (first_match and self.isMatch_v2(s, p, i + 1, j, memo)) or self.isMatch_v2(s, p, i, j + 2, memo)
                else:
                    match_result = first_match and self.isMatch_v2(s, p, i + 1, j + 1, memo)
            memo[i_j_pair] = match_result

        return memo[i_j_pair]


s1 = Solution()
s = "ab"
p = ".*c"
print(s1.isMatch(s, p))

