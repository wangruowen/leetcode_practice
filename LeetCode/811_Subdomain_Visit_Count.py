# https://leetcode.com/problems/subdomain-visit-count/description/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_counts = {}
        for each in cpdomains:
            each_count, each_domain = each.split()
            subdomains = [each_domain]
            dot_index = 0
            while True:
                dot_index = each_domain.find(".", dot_index)
                if dot_index < 0:
                    break
                dot_index += 1
                subdomains.append(each_domain[dot_index:])

            for each_subdomain in subdomains:
                domain_counts[each_subdomain] = \
                    domain_counts.get(each_subdomain, 0) + int(each_count)

        result = []
        for each_subdomain in domain_counts:
            result.append("%d %s" % (domain_counts[each_subdomain], each_subdomain))
        return result

s = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(s.subdomainVisits(cpdomains))
