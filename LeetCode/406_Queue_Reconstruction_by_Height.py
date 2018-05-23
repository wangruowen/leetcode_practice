# https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
        # 2. For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
        people.sort(key=lambda x: [x[0], -x[1]], reverse=True)
        result = people[:]
        for each in people:
            result.remove(each)
            result.insert(each[1], each)
        return result


s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))