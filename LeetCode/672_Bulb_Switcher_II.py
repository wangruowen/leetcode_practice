# https://leetcode.com/problems/bulb-switcher-ii/description/
class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Since n < 1000, we can also use bitmap
        n_status_set = set([tuple(True for _ in range(n))])
        for _ in range(m):
            new_status_set = self.helper(n_status_set)
            n_status_set = new_status_set
        return len(n_status_set)

    def helper(self, n_status_set):
        new_status_set = set()
        # Case 1: Flip all
        for each_status in n_status_set:
            new_status_set.add(tuple(map(lambda x: not x, each_status)))

        # print("Case 1: " + str(new_status_set))
        # Case 2: Flip even, but odd for 0-indexed list
        for each_status in n_status_set:
            new_status = tuple(not status if i % 2 != 0 else status for i, status in enumerate(each_status))
            new_status_set.add(new_status)
        # print("Case 2: " + str(new_status_set))
        # Case 3: Flip odd, but even for 0-indexed list
        for each_status in n_status_set:
            new_status = tuple(not status if i % 2 == 0 else status for i, status in enumerate(each_status))
            new_status_set.add(new_status)
        # print("Case 3: " + str(new_status_set))
        # Case 4: Flip 3k + 1
        for each_status in n_status_set:
            new_status = tuple(not status if (i + 1) % 3 == 1 else status for i, status in enumerate(each_status))
            new_status_set.add(new_status)
        # print("Case 4: " + str(new_status_set))

        return new_status_set

    def flipLights(self, n, m):
        # 1 + 2 --> 3, 1 + 3 --> 2, 2 + 3 --> 1
        # there are only 8 cases, all_on, all off, even on, even off, 3k + 1 on, 3k + 1 off and 1 + 4, 2 + 4, 3 + 4
        if n == 0 or m == 0: return 1
        if n == 1: return 2
        if n == 2 and m == 1: return 3
        if n == 2:
            # m > 1
            return 4
        if m == 1: return 4
        if m == 2:
            # All on, All off, Even On, Even off, 1 + 4, 2 + 4, 3 + 4,
            return 7
        if m >= 3: return 8
        return 8


s = Solution()
print(s.flipLights(1000, 1000))