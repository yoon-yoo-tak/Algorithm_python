# 네이버 공채 1번

import sys

input = sys.stdin.readline

import sys
input = sys.stdin.readline
n, Q, recent_day, recent_use, total_use = map(int, input().split())
recent = [0 for _ in range(n + 1)]
total = [0 for _ in range(n + 1)]
for _ in range(Q):
    day, idx, time = map(int, input().split())
    if day <= recent_day:
        recent[idx] += time
    total[idx] += time
ans = []
for i in range(1, n + 1):
    if recent[i] <= recent_use and total[i] < total_use:
        ans.append(i)
print(len(ans))
print(*ans)