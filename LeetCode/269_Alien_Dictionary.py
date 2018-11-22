# https://leetcode.com/problems/alien-dictionary/
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Topological Sort
        predecessor_map = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    # Only look at the first difference between two words
                    # because we don't know whether later letters are ordered
                    # e.g., abcf, abdz => c, d
                    # Here, predecessor_map[a] = b means, a is b's predecessor
                    predecessor_map.append([a, b])
                    break

        remain_letters = set("".join(words))
        order = []
        while predecessor_map:
            # Find the ones that don't have predecessors
            # in other words, their in-degree is 0
            has_predecesors = set([x[1] for x in predecessor_map])
            no_predecessor = remain_letters - has_predecesors
            if len(no_predecessor) == 0:
                # If all nodes have predecessors, then there must be loop existing.
                return ""
            order.extend(list(no_predecessor))
            predecessor_map = [x for x in predecessor_map if x[0] not in no_predecessor]
            remain_letters -= no_predecessor
        return "".join(order + list(remain_letters))


s = Solution()

