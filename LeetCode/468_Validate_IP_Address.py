# https://leetcode.com/problems/validate-ip-address/description/
import re

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ipv4_parts = IP.split(".")
        if len(ipv4_parts) > 1:
            # ipv4 candidate
            if len(ipv4_parts) != 4:
                return "Neither"
            for each in ipv4_parts:
                if len(each) == 0 or not each.isdigit() or str(int(each)) != each or int(each) < 0 or int(each) > 255:
                    return "Neither"
            return "IPv4"

        ipv6_parts = IP.split(":")
        ipv6_pattern = r'(?i)^[0-9a-f]{1,4}$'
        if len(ipv6_parts) > 1:
            # ipv6 candidate
            if len(ipv6_parts) != 8:
                return "Neither"
            for each in ipv6_parts:
                if not re.match(ipv6_pattern, each):
                    return "Neither"
            return "IPv6"

        return "Neither"

