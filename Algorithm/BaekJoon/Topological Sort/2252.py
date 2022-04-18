"""

2252 줄 세우기
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
con = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    con[x].append(y)
    indeg[y] += 1

q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

# 정렬할 수 있는 정점이 잇다면?
# 1. 정렬 결과에 추가하기
# 2. 정점과 연결된 간선 제거하기
# 3. 새롭게 "정렬될 수 있는" 정점 Queue 에 추가하기
while q:
    x = q.popleft()
    print(x, end=' ')
    for y in con[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)