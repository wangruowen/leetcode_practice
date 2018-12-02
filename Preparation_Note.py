# 1. For finding a substring (min or max) with certain pattern, we can often use a two pointers pattern
#     a. Base on the template of substring with start and cur pointers
#        https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
#        Template:

from collections import Counter, defaultdict
counter = Counter() / defaultdict / dict()
start, end = 0, 0
while end < len(s):
   counter[s[end]] += 1
   end += 1
   while Some Pattern happens or Not happens
       counter[s[start]] -= 1
       start += 1
       Until some pattern satistifed
       min_len = min(min_len, end - start)
   max_len = max(max_len, end - start)
return min_len or max_len

# 2. For some string, list, or pointers in a plane, with no orders, we may have to use Hashmap

# 3. Tree Traversal Iterative Ways

## Preorder Traversal Iterative
def preorder_iterative(node):
    if not node:
        return

    stack = [node]
    while stack:
        node = stack.pop()
        print(node.val)
        # Push right first, then left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

## Inorder Traversal Iterative
def inorder_iterative(node):
    if not node:
        return

    stack = []
    cur = node
    while cur or stack:
        # Keep DFS to the leftmost side
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.val)
        cur = cur.right

## Postorder Traversal Iterative
def postorder_iterative(node):
    if not node:
        return

    # This one is tricky
    # https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
    stack = []
    while node or stack:
        if node:
            if node.right
                stack.append(node.right)
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            if node.right and node.right == stack[-1]:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                print(node.val)
                node = None


# 4. String Subsequence often involves hashmap and DP

# 5. BFS backtracking needs to check visited before appending into the queue,
#    once appending into the queue, it should be marked as visited.
#    We cannot wait until q.popleft() and then mark visited. No! this is too late,
#    This could cause duplicates added into the queue.
#
#    DFS backtracking's visited.append() typically happens before recursively calling DFS, and pop() after the nested DFS.
