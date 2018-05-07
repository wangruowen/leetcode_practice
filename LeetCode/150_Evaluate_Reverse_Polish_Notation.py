# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Stack
        stack = []
        for token in tokens:
            if token in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(eval("int("+str(op2) + "." + token + str(op1)+")"))
            else:
                stack.append(int(token))

        return stack[-1]

s = Solution()
a = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(a))

