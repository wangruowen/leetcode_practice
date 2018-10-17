# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # Recursive call left of cur op and right of cur op
        if input.isdigit():
            return [int(input)]

        op_map = {"+": lambda x, y: x + y, "-": lambda x, y:x - y, "*": lambda x, y: x * y}
        result = []
        i = 0
        while i < len(input):
            if input[i] in "+-*":
                left_vals = self.diffWaysToCompute(input[:i])
                right_vals = self.diffWaysToCompute(input[i + 1:])
                for left in left_vals:
                    for right in right_vals:
                        result.append(op_map[input[i]](left, right))
            i += 1
        return result


s = Solution()
input = "2*3-4*5"
print(s.diffWaysToCompute(input))

