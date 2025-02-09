# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_count = {}
        ans = []
        for cp_domain in cpdomains:
            count, domain = cp_domain.split()
            count = int(count)
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                sub_domain = ".".join(subdomains[i:])
                domains_count[sub_domain] = domains_count.get(sub_domain, 0) + count
        return [f"{count} {subdomain}" for subdomain, count in domains_count.items()]