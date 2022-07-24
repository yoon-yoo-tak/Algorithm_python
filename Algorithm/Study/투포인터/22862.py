"""
22862 가장 긴 짝수 연속한 부분 수열(large)
"""
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
ls = list(map(int, input().split()))

l, r = 0, 0
odd = 0
ans = 0
length = 0

while l < n and r < n:
    if ls[l] % 2:
        if odd > 0:
            l += 1
            odd -= 1
        else:
            l += 1
            r = max(l, r)
    else:
        if ls[r] % 2:
            if odd >= k:
                if not ls[l] % 2:
                    length -= 1
                l += 1
            else:
                odd += 1
                r += 1
        else:
            length += 1
            r += 1
    ans = max(ans, length)
print(ans)