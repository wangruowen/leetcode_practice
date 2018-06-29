# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
class TrieNode(object):
    def __init__(self):
        self.children = {}

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Build a Trie Tree to capture 32-bit
        root = TrieNode()
        for each in nums:
            node = root
            for i in range(31, -1, -1):
                mask = 1 << i
                if each & mask == mask:
                    if 1 not in node.children:
                        tmp = TrieNode()
                        node.children[1] = tmp
                    node = node.children[1]
                else:
                    if 0 not in node.children:
                        tmp = TrieNode()
                        node.children[0] = tmp
                    node = node.children[0]

        max_xor = 0
        for each in nums:
            node = root
            cur_xor = 0
            for i in range(31, -1, -1):
                mask = 1 << i
                if each & mask == mask:
                    # bit 1 in cur item, we want to find bit 0, so that we can keep this bit as 1
                    if 0 in node.children:
                        cur_xor |= mask  # set current bit as 1
                        node = node.children[0]
                    else:
                        cur_xor &= ~mask # set current bit as 0
                        node = node.children[1]
                else:
                    # The opposite
                    if 1 in node.children:
                        cur_xor |= mask
                        node = node.children[1]
                    else:
                        cur_xor &= ~mask
                        node = node.children[0]
            max_xor = max(max_xor, cur_xor)

        return max_xor

s = Solution()
nums = [3,10, 5, 25, 2, 8]
print(s.findMaximumXOR(nums))




