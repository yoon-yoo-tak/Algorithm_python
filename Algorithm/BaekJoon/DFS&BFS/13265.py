"""

13265 색칠하기

"""
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

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
            if visit[i] == visit[n]:
                return False
    return True

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    color = [1, -1]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        if not visit[i]:
            ans = bfs(i, 1)
            if not ans:
                break
    print('possible' if ans else 'impossible')