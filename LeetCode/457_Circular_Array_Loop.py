# https://leetcode.com/problems/circular-array-loop/description/
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DFS
        i = 0
        total_visited = set()
        while i < len(nums):
            if i in total_visited:
                i += 1
                continue

            cur_visited = set([i])
            forward = 1 if nums[i] > 0 else -1
            j = i
            last = None
            while j < len(nums):
                if forward * nums[j] < 0:
                    break
                j += nums[j]
                j %= len(nums)
                if j in cur_visited:
                    if last != j:
                        return True
                    else:
                        break
                else:
                    cur_visited.add(j)
                    last = j
            total_visited.update(cur_visited)
            i += 1
        return False

s = Solution()
# nums = [2, -1, 1, 2, 2]
nums = [-1,2]
# nums = [-1, -2, -3, -4, -5]
print(s.circularArrayLoop(nums))