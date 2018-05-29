# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Get Three Max positives and Three Min negatives
        max_pos, min_neg = [], []
        has_zero = False
        for each in nums:
            if each > 0:
                if len(max_pos) < 3:
                    max_pos.append(each)
                else:
                    max_pos.append(each)
                    max_pos.sort()
                    max_pos.pop(0)
            elif each < 0:
                if len(min_neg) < 3:
                    min_neg.append(each)
                else:
                    min_neg.append(each)
                    min_neg.sort()
                    min_neg.pop()
            else:
                has_zero = True

        if len(max_pos) == 3 and len(min_neg) >= 2:
            max_pos_prod = max_pos[0] * max_pos[1] * max_pos[2]
            min_neg_prod = min_neg[0] * min_neg[1] * max_pos[2]
            return max(max_pos_prod, min_neg_prod)
        elif len(max_pos) < 3:
            # positive numbers are less than 3
            if len(max_pos) == 2:
                if len(min_neg) >= 2:
                    return min_neg[0] * min_neg[1] * max_pos[-1]
                elif has_zero:
                    return 0
                else:
                    return min_neg[-1] * max_pos[0] * max_pos[1]
            elif len(max_pos) == 1:
                if len(min_neg) >= 2:
                    return min_neg[0] * min_neg[1] * max_pos[-1]
                elif has_zero:
                    return 0
                else:
                    # Not possible, because the given array should be at least 3
                    return 0
            else:
                if has_zero:
                    return 0
                else:
                    # Find three max neg
                    max_neg = []
                    for each in nums:
                        if each < 0:
                            if len(max_neg) < 3:
                                max_neg.append(each)
                            else:
                                max_neg.append(each)
                                max_neg.sort()
                                max_neg.pop(0)
                    return max_neg[0] * max_neg[1] * max_neg[2]
        elif len(min_neg) < 2:
            # negative numbers are less than 2
            if len(max_pos) == 3:
                return max_pos[0] * max_pos[1] * max_pos[2]
            elif len(max_pos) == 2:
                if has_zero:
                    return 0
                else:
                    return min_neg[-1] * max_pos[0] * max_pos[1]
            else:
                return 0


s = Solution()
a = [1,2,3,4]
print(s.maximumProduct(a))
