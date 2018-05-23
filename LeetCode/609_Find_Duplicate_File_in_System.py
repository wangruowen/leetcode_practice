# https://leetcode.com/problems/find-duplicate-file-in-system/description/
import re

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_dict = {}
        for each_path in paths:
            path_contents = each_path.split()
            dir_path = path_contents[0]
            for each_file in path_contents[1:]:
                match = re.match(r'([^()]+)\(([^)]+)\)', each_file)
                file_name = match.group(1)
                content = match.group(2)
                content_dict[content] = content_dict.get(content, [])
                content_dict[content].append(dir_path + "/" + file_name)
        result = []
        # print(content_dict)
        for each_content in content_dict:
            if len(content_dict[each_content]) > 1:
                result.append(content_dict[each_content])

        return result

s = Solution()
paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(s.findDuplicate(paths))
