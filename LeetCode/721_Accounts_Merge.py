# https://leetcode.com/problems/accounts-merge/description/
class UnionFind(object):
    def __init__(self):
        self.set = []

    def get_id(self):
        self.set.append(len(self.set))
        return len(self.set)-1

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)

from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # Union Find
        unionfind = UnionFind()
        email2id, id2name = {}, {}
        for account in accounts:
            name = account[0]
            for each_email in account[1:]:
                if each_email not in email2id:
                    # get a new id
                    email2id[each_email] = unionfind.get_id()
                # Union ids of all emails with the id of the first email
                unionfind.union_set(email2id[account[1]], email2id[each_email])
            id2name[unionfind.find_set(email2id[account[1]])] = name

        id2emails = defaultdict(list)
        for email, id in email2id.items():
            id2emails[unionfind.find_set(id)].append(email)

        result = []
        for id, emails in id2emails.items():
            cur_account = [id2name[unionfind.find_set(id)]]
            cur_account += sorted(emails)
            result.append(cur_account)

        return result

s = Solution()
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

for each in s.accountsMerge(accounts):
    print(each)