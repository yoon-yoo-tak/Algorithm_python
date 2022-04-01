"""
프로그래머스 - 가장 먼 노드
"""

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    dist = [-1] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    def bfs(x):
        q = deque()
        q.append(x)
        dist[x] = 0
        while q:
            node = q.popleft()
            for i in graph[node]:
                if dist[i] != -1:
                    continue
                q.append(i)
                dist[i] = dist[node] + 1
    bfs(1)
    max_val = max(dist)
    answer = dist.count(max_val)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))