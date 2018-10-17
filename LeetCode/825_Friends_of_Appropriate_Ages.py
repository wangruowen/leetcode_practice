# https://leetcode.com/problems/friends-of-appropriate-ages/
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # age[B] > 100 > age[A] is a subset of age[B] > age[A]
        # So there are only two conditions
        # 1. age[B] <= 0.5 * age[A] + 7
        #      => When age[B] == age[A] and age[A] <= 14, we don't have friend
        # 2. age[B] > age[A]
        ages.sort()
        # Sliding Window
        start, cur = 0, 0
        result = 0
        while cur < len(ages):
            if ages[cur] <= 14:
                # condition 1: age[B] <= 14
                cur += 1
                continue
            # Look at ages <= cur
            while start < cur and ages[start] <= ages[cur] * 0.5 + 7:
                start += 1
            result += cur - start
            # Look at ages >= cur
            next = cur + 1
            while next < len(ages) and ages[cur] == ages[next]:
                next += 1
            result += next - 1 - cur
            cur += 1
        return result

s = Solution()
ages = [20,30,100,110,120]
print(s.numFriendRequests(ages))


