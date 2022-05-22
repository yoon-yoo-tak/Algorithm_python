"""
G or H 3
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = [0] * 10001
for _ in range(n):
    a, b = input().split()
    if b == 'G':
        ls[int(a)] = 1
    else:
        ls[int(a)] = 2

ans = -1
for i in range(10001 - k):
    ans = max(ans, sum(ls[i:i + k + 1]))
print(ans)