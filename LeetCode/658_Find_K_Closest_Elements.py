class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        diff_map = {}  # diff -> list of item indices
        for each in arr:
            diff = abs(each - x)
            if diff in diff_map:
                diff_map[diff].append(each)
            else:
                diff_map[diff] = [each]

        result = []
        sorted_keys = sorted(diff_map.keys())
        cur_key_index = 0
        while len(result) < k:
            cur_key = sorted_keys[cur_key_index]
            cur_key_items = sorted(diff_map[cur_key])
            if len(cur_key_items) + len(result) <= k:
                result.extend(cur_key_items)
                cur_key_index += 1
            else:
                num_to_take = k - len(result)
                result.extend(cur_key_items[:num_to_take])
                diff_map[cur_key] = cur_key_items[num_to_take:]

        return sorted(result)

s = Solution()
arr = [1,2,3,4,5]
k = 4
x = -1
print(s.findClosestElements(arr, k, x))


