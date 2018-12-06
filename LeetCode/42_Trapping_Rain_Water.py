# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, result = [], 0
        for i, h in enumerate(height):
            if not stack:
                stack.append((i, h))
            else:
                # h > last stack height, we need to find its left and right
                while stack and stack[-1][1] < h:
                    last_i, last_h = stack.pop()
                    if stack:
                        left_i, left_h = stack[-1]
                        # compare its left and right side height and fill the water
                        result += (min(left_h, h) - last_h) * (i - left_i - 1)
                stack.append((i, h))

        return result


s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4, 2, 0, 3, 2, 5]
print(s.trap(height))


