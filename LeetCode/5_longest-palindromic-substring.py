class Solution(object):
    def __init__(self):
        self.max_palindrome = ""
        self.cached_check = {}

    def longestPalindrome(self, s):
        for i in xrange(len(s)):
            # Expand odd first
            odd_pal = self.expand_palindrome(s, i, i)
            if len(odd_pal) > len(self.max_palindrome):
                self.max_palindrome = odd_pal
            even_pal = self.expand_palindrome(s, i, i + 1)
            if len(even_pal) > len(self.max_palindrome):
                self.max_palindrome = even_pal

        return self.max_palindrome

    def expand_palindrome(self, s, l, r):
        """
        if l == r from the start, we expand odd palindrome
        if l, r next to each other, we expand even palindrome
        :param s:
        :param l:
        :param r:
        :return:
        """
        has_expanded = False
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            has_expanded = True
        if has_expanded:
            pal_str = s[l + 1:r]
            return pal_str
        else:
            return ""

    def longestPalindrome_v1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        if len(s) == 2:
            if self.is_palindrome(s):
                return s
            else:
                return s[0]

        # Now for len(s) >= 3
        self.max_palindrome = ""
        for start in xrange(len(s)):
            last_max_len = len(self.max_palindrome)
            cur = len(s)  # start from the longest length
            while cur > start + last_max_len:
                str_to_check = s[start:cur]
                if str_to_check in self.cached_check:
                    if self.cached_check[str_to_check]:
                        break
                    else:
                        cur -= 1
                else:
                    if self.is_palindrome(str_to_check) and len(str_to_check) > len(self.max_palindrome):
                        self.max_palindrome = str_to_check
                        break
                    else:
                        cur -= 1

        return self.max_palindrome

    def is_palindrome(self, str_val):
        self.cached_check[str_val] = str_val == str_val[::-1]
        return self.cached_check[str_val]

    @staticmethod
    def is_palindrome_v2(str_val):
        """
        Or as simple as the following
        return str_val == str_val[::-1]
        :param str_val:
        :return:
        """
        half_len = len(str_val) / 2
        i = 0
        result = True
        while i < half_len:
            if str_val[i] == str_val[-1 - i]:
                i += 1
            else:
                result = False
                break

        return result

    def longestPalindrome_v2(self, s, one_side_of_pan=""):
        """
        In this version, we do a recursion.
        :param s:
        :return:
        """
        if len(s) < 2:
            return one_side_of_pan + s + one_side_of_pan[::-1]
        if len(s) == 2:
            if self.is_palindrome(s):
                return one_side_of_pan + s + one_side_of_pan[::-1]
            else:
                return ""

        if s[0] == s[-1]:
            one_side_of_pan += s[0]
            return self.longestPalindrome_v2(s[1:-1], one_side_of_pan)
        else:
            max_pan1 = self.longestPalindrome_v2(s[:-1])
            max_pan2 = self.longestPalindrome_v2(s[1:])
            if len(max_pan1) > len(max_pan2):
                return max_pan1
            else:
                return max_pan2



s = Solution()
print(s.longestPalindrome_v2(
# "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
# "abab"
#     "abaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaba"
"jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
))
