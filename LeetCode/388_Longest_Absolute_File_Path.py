# https://leetcode.com/problems/longest-absolute-file-path/
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Stack
        input += "\n"  # padding one last for the following while loop
        max_len = 0
        offset = input.find("\n")  # Use find instead of index, because index throw Error
        stack = [input[:offset]]
        while input.find("\n", offset + 1) >= 0:
            new_offset = input.find("\n", offset + 1)
            if new_offset < 0:
                new_offset = len(input)
            cur_dir = input[offset + 1:new_offset]
            num_of_tabs = cur_dir.count("\t")
            if num_of_tabs < len(stack):
                # When num_of_tabs < len(stack), Previous one is deeper
                # It is impossible that num_of_tabs > len(stack)
                if stack[-1].find('.') >= 0 and stack[-1][-1] != '.':
                    # print("/".join(stack))
                    max_len = max(max_len, len("/".join(stack)))
                while num_of_tabs < len(stack):
                    stack.pop()
            stack.append(cur_dir[num_of_tabs:])
            offset = new_offset

        # Last one
        if stack[-1].find('.') >= 0 and stack[-1][-1] != '.':
            # print("/".join(stack))
            max_len = max(max_len, len("/".join(stack)))

        return max_len

s = Solution()
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.lengthLongestPath(input))


