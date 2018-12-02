# https://leetcode.com/problems/factor-combinations/
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Not working, has duplicates
        factors = []
        i = 2
        n_sqrt = int(n ** 0.5)
        N = n
        while i <= n_sqrt:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1

        # print(factors)

        result = set()
        def helper(i, stack):
            if i == len(factors) and stack and stack[0] != N:
                result.add(stack[:])
                return

            cur = 1
            for j in range(i, len(factors)):
                cur *= factors[j]
                stack.append(cur)
                helper(j + 1, stack)
                stack.pop()

        helper(0, [])
        return list(result)

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result, stack, i = [], [], 2
        while True:
            if i > n // i:
                if not stack:
                    return result
                # Backward pop back
                result.append(stack + [n])
                i = stack.pop()
                n *= i
                i += 1
            elif n % i == 0:
                stack.append(i)
                n //= i
            else:
                i += 1

s = Solution()
n = 12
print(s.getFactors(n))
