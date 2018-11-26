# https://leetcode.com/problems/kill-process/
from collections import defaultdict

class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # BFS
        children_map = defaultdict(list)
        for k, v in zip(ppid, pid):
            children_map[k].append(v)

        result = []
        to_kill = [kill]
        while to_kill:
            cur_pid = to_kill.pop(0)
            result.append(cur_pid)
            for each_child_pid in children_map[cur_pid]:
                to_kill.append(each_child_pid)
        return result
