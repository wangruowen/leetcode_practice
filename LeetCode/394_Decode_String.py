# https://leetcode.com/problems/decode-string/description/
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        k = 0
        s_to_repeat = ""
        result = ""
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                # start of the to-be-repeated string
                if len(stack) > 0:
                    # We already have previous '[' and previous s_to_repeat
                    stack.append(s_to_repeat)
                stack.append(k)
                k, s_to_repeat = 0, ""
            elif c == ']':
                # end of the string
                cur_k = stack.pop()
                if len(stack) > 0:
                    prev_s_to_repeat = stack.pop()
                    s_to_repeat = prev_s_to_repeat + cur_k * s_to_repeat
                else:
                    result += cur_k * s_to_repeat
            else:
                if len(stack) == 0:
                    result += c
                else:
                    s_to_repeat += c

        return result

s = Solution()
S = "2[abc]3[cd]ef"
print(s.decodeString(S))