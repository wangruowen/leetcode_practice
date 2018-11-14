# http://www.cnblogs.com/grandyang/p/6828353.html
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(candidates):
            i, j = 0, len(candidates) - 1
            pairs = []
            while i < j:
                pairs.append((candidates[i], candidates[j]))
                i += 1
                j -= 1
            # print(pairs)
            if len(pairs) > 1:
                return helper(tuple(pairs))
            else:
                return tuple(pairs)
        pairs = helper(tuple(range(1, n+1)))
        return str(pairs[0])

s = Solution()
print(s.findContestMatch(16))
