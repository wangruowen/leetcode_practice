# 1. create a 2D array must be
a = [[False for i in range(self.col_num)] for j in range(self.row_num)]
# not
# a = [[False] * 5] * 5

# 2. sorted(array) does not modify the original array
# array.sort() sorts the array in place

# 3 Reverse a linked list
last, cur = None, head
while cur:
    tmp = cur.next
    cur.next = last
    last = cur
    cur = tmp

head = last

# 4. Binary Search
def _binary_search(self, nums, target):
    """
    When end is exclusive, the while loop condition is start < end
    then end = mid, start = mid + 1
    """
    start, end = 0, len(nums)
    while start < end:
        mid = (start + end) / 2
        if target < nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    return -1

def _binary_search(self, nums, target):
    """
    When end is inclusive, the while loop condition is start <= end
    then end = mid - 1, start = mid + 1
    """
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    return -1

# 5. Check if the given string is a palindrome
i, j = 0, len(s) - 1
while i < j:
    if s[i] != s[j]:
        return False
    i += 1
    j -= 1
return True

# 6. To memoize if one substring is a palindrome
# dp[i][j] refers to whether s[i:j] is a palindrome
for i in range(len(s)):
    dp[i][i] = True
    if i < len(s) - 1 and s[i] == s[i+1]:
        dp[i][i+1] = True

for length in range(2, len(s)):
    for i in range(len(s) - length):
        j = i + length
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]

# 7. Prime Factorization
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac