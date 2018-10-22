# http://www.cnblogs.com/grandyang/p/5310649.html
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Greedy Suppose celebrity is 0
        celebrity_i = 0

        for i in range(1, n):
            if celebrity_i != i and knows(celebrity_i, i):
                # if celebrity knows i, let i become celebrity
                celebrity_i = i

        for i in range(n):
            if i == celebrity_i:
                continue
            if knows(celebrity_i, i) or not knows(i, celebrity_i):
                return -1
        return celebrity_i
