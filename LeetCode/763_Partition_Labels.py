# https://leetcode.com/problems/partition-labels/description/
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Greedy
        # Incrementally check each letter, if it has appeared in previous part,
        # merge all parts since that part into one part
        parts = []
        for each_letter in S:
            prev_part = -1
            for i in range(len(parts)):
                if each_letter in parts[i]:
                    prev_part = i
                    break
            if prev_part >= 0:
                new_part = "".join(parts[i:]) + each_letter
                parts = parts[:i] + [new_part]
                # print("new_part: " + new_part)
                # print("parts: " + str(parts))
            else:
                parts.append(each_letter)
        return [len(x) for x in parts]

s = Solution()
S = "ababcbacadefegdehijhklij"
print(s.partitionLabels(S))


