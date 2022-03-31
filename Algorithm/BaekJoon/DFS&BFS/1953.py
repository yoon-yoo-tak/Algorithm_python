"""
1953 팀배분


"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
for i in range(1, n + 1):
    a, *b = list(map(int, input().split()))
    for num in b:
        graph[i].append(num)

def bfs(v, group):
    q = deque()
    q.append(v)
    visit[v] = group
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visit[i]:
                q.append(i)
                visit[i] = -1 * visit[n]

for i in range(1, n + 1):
    if not visit[i]:
        bfs(i, 1)

print(visit.count(1))
for i in range(len(visit)):
    if visit[i] == 1:
        print(i, end=' ')
print()
print(visit.count(-1))
for i in range(len(visit)):
    if visit[i] == -1:
        print(i, end=' ')