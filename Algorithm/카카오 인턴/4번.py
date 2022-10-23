from collections import deque


def solution(n: int, paths: list, gates: list, summits: list) -> list:
    result = []
    is_summits = [False] * 5005
    for i in range(len(summits)):
        is_summits[summits[i]] = True
    summits.sort()
    graph = [[] * (len(paths) + 1) for _ in range(len(paths) + 1)]
    for x, y, c in paths:
        graph[x].append([y, c])
        graph[y].append([x, c])
    ansV, ansSummit = 0, 0
    visited = [False] * (n + 1)
    def bfs(s, X):
        q = deque()
        q.append(s)
        visited[s] = True
        while q:
            x = q.popleft()
            if is_summits[x]:
                continue
            for y, c in graph[x]:
                if c > X:
                    continue
                if visited[y]:
                    continue
                visited[y] = 1
                q.append(y)
    def check(X):
        nonlocal visited
        visited = [False] * (n + 1)
        for i in range(n + 1):
            if visited[i]:
                continue
            bfs(gates[i], X)
        for i in range(len(summits)):
            if visited[summits[i]]:
                ansV = X
                ansSummit = summits[i]
                return True
        return False

    l, r = 1, 10000000
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1

    return [ansSummit, ansV]




print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
