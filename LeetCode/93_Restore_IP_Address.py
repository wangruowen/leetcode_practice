# https://leetcode.com/problems/restore-ip-addresses/description/
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Backtrack
        all_ips = []
        self.helper(s, 4, all_ips, [])
        return all_ips

    def helper(self, rest_s, parts, all_ips, exist_set):
        if parts == 0 and len(rest_s) == 0:
            all_ips.append(".".join(exist_set))
            return
        elif parts == 0 or len(rest_s) == 0:
            return

        # Get all valid ones from rest_s
        if int(rest_s[:1]) >= 0:
            exist_set.append(rest_s[:1])
            self.helper(rest_s[1:], parts - 1, all_ips, exist_set)
            exist_set.pop()
        if int(rest_s[:2]) >= 10:
            exist_set.append(rest_s[:2])
            self.helper(rest_s[2:], parts - 1, all_ips, exist_set)
            exist_set.pop()
        if int(rest_s[:3]) >= 100 and int(rest_s[:3]) <= 255:
            exist_set.append(rest_s[:3])
            self.helper(rest_s[3:], parts - 1, all_ips, exist_set)
            exist_set.pop()


s = Solution()
s1 = "25525511135"
print(s.restoreIpAddresses(s1))





