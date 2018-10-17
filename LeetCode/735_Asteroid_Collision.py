# https://leetcode.com/problems/asteroid-collision/description/
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for each in asteroids:
            if len(stack) == 0:
                stack.append(each)
            else:
                cur_explode = False
                while each < 0 and len(stack) > 0 and stack[-1] > 0:
                    # Can collide
                    if abs(each) > abs(stack[-1]):
                        stack.pop()
                    elif abs(each) == abs(stack[-1]):
                        cur_explode = True
                        stack.pop()
                        break
                    else:
                        cur_explode = True
                        break
                if not cur_explode:
                    stack.append(each)
        return stack

s = Solution()
asteroids = [1, -2, -2, -2]
print(s.asteroidCollision(asteroids))
