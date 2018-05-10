# https://leetcode.com/problems/daily-temperatures/description/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Stack, same as Next Greater Element
        stack, result = [], [0 for _ in temperatures]
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result

s = Solution()
t = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(t))

