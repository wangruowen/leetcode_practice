# https://leetcode.com/problems/online-election/
import bisect
from collections import Counter

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # As the votes come in, we can remember every event (winner, time) when the winner changes. After, we have a sorted list of these events that we can binary search for the answer.
        self.A = []
        counter = Counter()
        cur_leader, cur_max_votes = None, 0
        for p, t in zip(persons, times):
            counter[p] += 1
            if counter[p] >= cur_max_votes:
                if cur_leader != p:
                    cur_leader = p
                    self.A.append((t, cur_leader))
                cur_max_votes = counter[p]


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = bisect.bisect_right(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)