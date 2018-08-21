# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder_list = preorder.split(",")
        if preorder_list[0] == '#':
            if len(preorder_list) > 1:
                return False
            else:
                return True
        stack = [True]  # The stack keeps current node's parent and whether this parent is the left or right child of its own parent
        i = 1
        is_right = False
        while i < len(preorder_list):
            if preorder_list[i] == '#':
                if is_right:
                    # Both children of the previous parent are visited
                    # pop the parent. if stack is empty, something wrong
                    if len(stack) > 0:
                        # If parent is right node, we keep popping
                        top = stack.pop()
                        while len(stack) > 0 and top:
                            top = stack.pop()
                        if len(stack) == 0 and i < len(preorder_list) - 1:
                            # stack should never be empty because we have the root node
                            return False
                    else:
                        return False
                else:
                    is_right = not is_right
            else:
                # Encounter a new node, push into stack and wait for visiting its children
                stack.append(is_right)
                # Next should be the left child
                is_right = False
            i += 1

        return len(stack) == 0

s = Solution()
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(s.isValidSerialization(preorder))