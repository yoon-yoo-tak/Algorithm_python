"""
2623 음악 프로그램

"""

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
con = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(2, len(order)):
        con[order[i - 1]].append(order[i])
        indeg[order[i]] += 1

q = deque()

for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

res = []
while q:
    x = q.popleft()
    res.append(x)
    for y in con[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)

if len(res) != n:
    print(0)
else:
    for x in res:
        print(x)