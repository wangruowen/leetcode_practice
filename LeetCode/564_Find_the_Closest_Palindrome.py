# https://leetcode.com/problems/find-the-closest-palindrome/description/
class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # If len(result) == len(n), then we should choose from first_half(n) (+1,-1,0)
        # If len(result) > len(n), then it must be 10**len(n) + 1
        # If len(result) < len(n), then it must be 10**(len(n) - 1) - 1
        len_n = len(n)
        candidates = set([str(10**len_n + 1), str(10**(len_n - 1) - 1)])
        if len_n % 2 == 0:
            first_half = int(n[:len_n // 2])
            for i in [1, -1, 0]:
                palindrome = str(first_half + i) + str(first_half + i)[::-1]
                candidates.add(palindrome)
        else:
            first_half = int(n[:(len_n + 1) // 2])
            for i in [1, -1, 0]:
                new_half = first_half + i
                palindrome = str(new_half) + str(new_half)[:-1][::-1]
                candidates.add(palindrome)
        min_palindrome = None
        min_diff = float('inf')
        for each in candidates:
            if each == n: continue
            cur_diff = abs(int(each) - int(n))
            if cur_diff < min_diff:
                min_diff = cur_diff
                min_palindrome = each
            elif cur_diff == min_diff and int(each) < int(min_palindrome):
                min_palindrome = each
        return min_palindrome

s = Solution()
print(s.nearestPalindromic("3"))
