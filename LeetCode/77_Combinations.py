import datetime

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums_set = [i for i in range(1, n + 1)]
        return self.combine_helper(nums_set, k)

    def combine_helper(self, nums, k):
        """
        Select k items from a set of nums equals:
        (1) pick one item, recursively get the k - 1 combination of the rest n - 1 item, and add this item to each of the k - 1 combination
        (2) without this item, the k combination of the rest n - 1 nums
        (3) Sum (1) and (2) together
        :param nums:
        :param k:
        :return:
        """
        if k >= len(nums):
            return [[i for i in nums]]

        result_comb = []

        if k == 1:
            for i in range(len(nums)):
                result_comb.append([nums[i]])
        else:
            cur_num = nums[0]
            for each_comb in self.combine_helper(nums[1:], k - 1):
                each_comb.insert(0, cur_num)
                result_comb.append(each_comb)
            without_cur_num_comb = self.combine_helper(nums[1:], k)
            result_comb.extend(without_cur_num_comb)

        return result_comb

    def combine_v2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def helper(nums, stack, k):
            if k == 0:
                result.append(stack[:])
                return
            if not nums:
                return

            for i, c in enumerate(nums):
                stack.append(c)
                helper(nums[i + 1:], stack, k - 1)
                stack.pop()

        helper(list(range(1, n + 1)), [], k)
        return result
s = Solution()
start_time = datetime.datetime.now()
print(s.combine(20, 16))
end_time = datetime.datetime.now()
print("Time spent: %s" % (end_time - start_time))
