# https://leetcode.com/problems/compare-version-numbers/description/
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        i += 1
        while i < len(v1):
            if int(v1[i]) > 0:
                return 1
            i += 1
        while i < len(v2):
            if int(v2[i]) > 0:
                return -1
            i += 1
        return 0