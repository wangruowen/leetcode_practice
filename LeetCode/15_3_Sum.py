
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_list = []

        if len(nums) < 3:
            return ret_list

        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == 0:
                    ret_list.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return ret_list

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
