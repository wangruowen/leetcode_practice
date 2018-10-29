# http://www.cnblogs.com/grandyang/p/5595614.html
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # High school math
        result = []
        i, j = 0, len(nums)
        def f(x):
            return a * x ** 2 + b * x + c

        d = -1 if a > 0 else 1
        while i <= j:
            if d * f(nums[i]) < d * f(nums[j]):
                result.append(f(nums[i]))
                i += 1
            else:
                result.append(f(nums[j]))
                j -= 1
        return result[::-1]


