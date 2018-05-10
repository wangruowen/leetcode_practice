# https://leetcode.com/problems/next-greater-element-iii/description/
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If the last few digits are:
        # 1. n[-2] < n[-1] => swap them, like 123 => 132
        # 2. n[-2] >= n[-1] =>
        # Find the previous num not decreasing,
        # replace with the smallest greater num and re-order the rest as increasing
        # like 124765 => 125467
        n_array = map(int, list(str(n)))
        if len(n_array) <= 1:
            return -1
        if len(n_array) == 2:
            if n_array[0] < n_array[1]:
                return int("".join(map(str, n_array[::-1])))
            else:
                return -1

        if n_array[-2] < n_array[-1]:
            # swap them
            n_array[-2], n_array[-1] = n_array[-1], n_array[-2]
            new_n = int("".join(map(str, n_array)))
        else:
            i = len(n_array) - 1
            while i > 0 and n_array[i - 1] >= n_array[i]:
                i -= 1
            if i == 0:
                # The n_array is completely decreasing
                return -1
            else:
                new_array = n_array[:i - 1]
                # Replace i - 1 th item with the smallest greater item in n_array[i:]
                for j in range(len(n_array) - 1, i - 1, -1):
                    if n_array[j] > n_array[i - 1]:
                        break
                new_array.append(n_array[j])
                n_array[j] = n_array[i - 1]
                new_array.extend(reversed(n_array[i:]))
                new_n = int("".join(map(str, new_array)))
        return new_n if new_n <= 2 ** 31 else -1

s = Solution()
print(s.nextGreaterElement(54321))
