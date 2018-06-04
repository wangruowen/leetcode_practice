# https://leetcode.com/problems/rabbits-in-forest/description/
from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if len(answers) == 0:
            return 0

        counter = Counter(answers)
        result = 0
        for each_key in counter:
            each_count = counter[each_key]
            if each_key + 1 == each_count:
                # All rabbits in this color have reported answer
                result += each_count
            elif each_key + 1 > each_count:
                # There are some rabbits in this color not reporting
                result += each_key + 1
            else:
                # each_key + 1 < each_count
                # There should be two different colors
                result += each_count / (each_key + 1) * (each_key + 1)
                if each_count % (each_key + 1) > 0:
                    result += each_key + 1
        return result

s = Solution()
answers = [1,0,1,0,0]
print(s.numRabbits(answers))
