# https://leetcode.com/problems/shortest-distance-to-a-character/description/
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_indices = []
        for i in range(len(S)):
            if S[i] == C:
                c_indices.append(i)

        result = [0] * len(S)
        c_index = 0
        prev_c_index, next_c_index = -1, c_indices[c_index]
        for i in range(len(S)):
            if S[i] != C:
                if prev_c_index < 0:
                    result[i] = abs(i - next_c_index)
                elif next_c_index < 0:
                    result[i] = abs(i - prev_c_index)
                else:
                    result[i] = min(abs(i - prev_c_index), abs(i - next_c_index))
            else:
                prev_c_index = next_c_index
                c_index += 1
                next_c_index = c_indices[c_index] if c_index < len(c_indices) else -1
                result[i] = 0

        return result

s = Solution()
S = "loveleetcode"
C = 'e'
print(s.shortestToChar(S, C))