"""

11724 연결 요소


"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visit[v] = True
    q = deque([v])
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        cnt += 1

print(cnt)
