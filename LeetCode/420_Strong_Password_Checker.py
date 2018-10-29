# https://leetcode.com/problems/strong-password-checker
class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_types = 3
        if any('a' <= c <= 'z' for c in s):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in s):
            missing_types -= 1
        if any(c.isdigit() for c in s):
            missing_types -= 1

        can_replace, can_delete_one, can_delete_two, can_delete_three = 0, 0, 0, 0
        i = 2
        while i < len(s):
            if s[i] == s[i-1] == s[i-2]:
                length = 3
                i += 1
                while i < len(s) and s[i] == s[i-1]:
                    length += 1
                    i += 1

                # 1. If we want to replace, how many we need to replace
                can_replace += length // 3  # Replace one letter per 3 same letters is always less than or equal to delete

                # 2. If we want to delete to save replace, how many we need to delete
                if length % 3 == 0:
                    # e.g., we can do aaa => aa instead of aaa => aab
                    # Note that, if length is aaa|aaa|aaa, we can only delete one letter and the rest two have to be replaced
                    can_delete_one += 1
                elif length % 3 == 1:
                    # e.g., we do aaaa => aa instead of aaaa => aaba
                    # If aaa|aaa|a => we can delete 2 to save 1 replace, aaa|aa => aabaa, otherwise, it needs 2 replaces aab|aab|a
                    can_delete_two += 1
                # elif length % 3 == 2:
                #     # e.g., aaa|aaa|aa => we can delete 3 to save 1 replace
                #     can_delete_three += 1
            else:
                i += 1
        if len(s) < 6:
            return max(missing_types, 6 - len(s))
        elif len(s) <= 20:
            return max(can_replace, missing_types)
        else:
            deletion = len(s) - 20

            print(deletion, can_replace, can_delete_one, can_delete_two, can_delete_three, missing_types)

            # As the goal is to minimize operations, we start from can_delete_one, because it is a 1 to 1 mapping between one delete and one replace
            if deletion <= can_delete_one:
                can_replace -= deletion
            else:
                can_replace -= can_delete_one
                deletion -= can_delete_one
            if deletion > 0:
                if deletion <= can_delete_two * 2:
                    can_replace -= deletion // 2
                else:
                    can_replace -= can_delete_two
                deletion -= can_delete_two * 2
            if deletion > 0:
                can_replace -= deletion // 3

            return len(s) - 20 + max(missing_types, can_replace)

s = Solution()
test = "aaaaaa1234567890123Ubefg"
print(s.strongPasswordChecker(test))