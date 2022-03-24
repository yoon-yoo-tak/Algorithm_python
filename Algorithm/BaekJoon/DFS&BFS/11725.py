"""

11725 트리의 부모 찾기

1번이 루트라고 가정했을때 각 노드의 부모 노드를 출력

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(k):
    q = deque([k])
    visit[k] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = x
                q.append(i)

bfs(1)
for i in range(2, n + 1):
    print(visit[i])