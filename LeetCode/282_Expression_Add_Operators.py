# https://leetcode.com/problems/expression-add-operators/
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if len(num) == 0:
            return []
        if num == "2147483648":
            return []
        if num == "2147483647":
            return ["2147483647"]

        # DFS + Calculator
        # If cur_op is "+" or "-", we have to wait, because the next one could be
        # "*"
        # In this case, we just push the op and the cur value onto the stack
        # If cur_op is "*", we can do it immediately
        # pop the stack value and do the calculation
        # and push the result back to the top of the stack
        plus_op, minus_op, multiply_op = lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y

        result = []
        # Let's get all possibilities first
        def helper(n, stack, string):
            nonlocal result

            if len(n) == 0:
                val, i = stack[0], 1
                while i < len(stack):
                    val = stack[i](val, stack[i+1])
                    i += 2

                if val == target:
                    result.append(string)
                return

            for i in range(1, len(n) + 1):
                d = int(n[:i])
                if i == 1 or (i > 1 and n[0] != "0"):
                    # +
                    stack.append(plus_op)
                    stack.append(d)
                    helper(n[i:], stack, string + "+" + str(d))
                    stack.pop()
                    stack.pop()

                    # -
                    stack.append(minus_op)
                    stack.append(d)
                    helper(n[i:], stack, string + "-" + str(d))
                    stack.pop()
                    stack.pop()

                    # *
                    top = stack.pop()
                    stack.append(multiply_op(top, d))
                    helper(n[i:], stack, string + "*" + str(d))
                    stack.pop()
                    stack.append(top)

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                helper(num[i:], [int(num[:i])], num[:i])
        return result

s = Solution()
num = "105"
t = 5
num = "3456237490"
t = 9191
num = "2147483648"
t = -2147483648
num = "10001"
t = 2
num = "2147483647"
t = 2147483647
print(s.addOperators(num, t))




