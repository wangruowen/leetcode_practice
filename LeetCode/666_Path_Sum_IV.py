# https://leetcode.com/problems/path-sum-iv/
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_level = 1
        last_level_path = {1: 0}
        result = 0
        while nums:
            cur_level_nodes, cur_level_path = [], {}
            while nums:
                if nums[0] // 100 == cur_level:
                    cur_level_nodes.append(nums.pop(0) % 100)
                else:
                    break

            parents_visited = set()
            for each in cur_level_nodes:
                pos = each // 10
                parent_pos = (pos + 1) // 2
                cur_level_path[pos] = last_level_path[parent_pos] + each % 10
                parents_visited.add(parent_pos)
            for each_parent_pos in last_level_path:
                if each_parent_pos not in parents_visited:
                    # Parent is leaf
                    result += last_level_path[each_parent_pos]

            last_level_path = cur_level_path
            cur_level += 1
        return sum(last_level_path.values()) + result


s = Solution()
nums = [111,217,221,315,415]
print(s.pathSum(nums))
