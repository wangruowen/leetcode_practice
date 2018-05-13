# https://leetcode.com/problems/employee-importance/description/
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        total_important = 0
        root = None
        employee_map = {}
        for each in employees:
            employee_map[each.id] = each

        # BFS
        queue = [employee_map[id]]
        while len(queue) > 0:
            cur = queue.pop(0)
            total_important += cur.importance
            for each_sub_id in cur.subordinates:
                queue.append(employee_map[each_sub_id])

        return total_important
