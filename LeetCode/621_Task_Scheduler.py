# https://leetcode.com/problems/task-scheduler/description/
from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # If n = 3
        # A___A___A
        # Either the idle intervals are more than remaining tasks (Still has idle intervals in the result)
        # ABC_AB
        # Or all tasks take turn to happen which is just the tasks.length (No idle interval)
        # ABCDABC
        counter = Counter(tasks)
        highest_freq = max(counter.values())
        highest_count = counter.values().count(highest_freq)
        # if highest_count <= n:
        #     we may still have idle intervals
        # if highest_count > n or less-frequent tasks overflow the idle slots:
        #     tasks.length is the max length

        # (highest_freq - 1) * (n + 1) is ABC___ABC___
        # highest_count is the last ABC
        return max(len(tasks), (highest_freq - 1) * (n + 1) + highest_count)




