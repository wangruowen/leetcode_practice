# https://leetcode.com/problems/unique-email-addresses/
import re

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for each in emails:
            local, domain = each.split('@')
            local = re.sub(r'(\.|\+.*$)', '', local)
            unique_emails.add("%s@%s" % (local, domain))
        return len(unique_emails)