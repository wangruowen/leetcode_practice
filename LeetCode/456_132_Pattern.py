# https://leetcode.com/problems/132-pattern/description/
class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # s1 < s3 < s2
        stack = []
        max_s3 = float('-inf')
        for each in reversed(nums):
            if each < max_s3:
                # Here, each is s1
                # if we get here, it means we found s1 < s3, plus previous s3 < s2
                return True
            else:
                while len(stack) > 0 and each > stack[-1]:
                    # Here, each is s2
                    # if we get here, it means we found s2 > s3
                    max_s3 = stack.pop()
            stack.append(each)
        return False
