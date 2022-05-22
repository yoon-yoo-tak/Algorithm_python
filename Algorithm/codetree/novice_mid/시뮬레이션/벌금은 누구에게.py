"""

"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
num = [0] * (n + 1)
order = [int(input()) for _ in range(m)]
ans = 0
for i in order:
    num[i] += 1
    if num[i] == k:
        ans = i
        break
print(-1 if ans == 0 else ans)
