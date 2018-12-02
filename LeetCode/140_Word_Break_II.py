# https://leetcode.com/problems/word-break-ii/
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = None

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def buildTrie():
            root = TrieNode("")
            for word in wordDict:
                cur = root
                for c in word:
                    if c not in cur.children:
                        node = TrieNode(c)
                        cur.children[c] = node
                    cur = cur.children[c]
                cur.word = word
            return root

        def searchTrie(word, root, cache):
            if word in cache:
                return cache[word]

            cur = root
            for c in word:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            cache[word] = cur.word == word
            return cache[word]

        root = buildTrie()
        result = []
        cache = {}
        def helper(i, stack):
            nonlocal root, result

            if i == len(s):
                result.append(" ".join(stack))
                return

            for j in range(i + 1, len(s) + 1):
                if searchTrie(s[i:j], root, cache):
                    stack.append(s[i:j])
                    helper(j, stack)
                    stack.pop()
        helper(0, [])
        return result

    def wordBreak_v2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in range(n + 1)]
        valid = [[False] * n for _ in range(n)]
        can_break[0] = True
        for i in range(1, n + 1):
            for l in range(1, min(i, max_len) + 1):
                if can_break[i - l] and s[i - l:i] in wordDict:
                    valid[i - l][i - 1] = True
                    can_break[i] = True

        result = []
        if can_break[-1]:
            self.wordBreakHelper(s, valid, 0, [], result)
        return result

    def wordBreakHelper(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return
        for i in range(start, len(s)):
            if valid[start][i]:
                path += [s[start:i + 1]]
                self.wordBreakHelper(s, valid, i + 1, path, result)
                path.pop()


s = Solution()
# t = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
t = "aaaaaaaaaaaaa"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(s.wordBreak(t, d))
