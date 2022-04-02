"""

1707 이분 그래프

"""
import sys
from collections import deque

input = sys.stdin.readline

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


t = int(input())


for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visit = [False] * (v + 1)
    color = [-1, 1]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visit[i]:
            ans = bfs(i, 1)
            if not ans:
                break
    print('YES' if ans else 'NO')
