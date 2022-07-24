"""
17304 변호사들
양방향 안됨.
"""
import sys
input = sys.sstdin.readline

def dfs(node, prev):
    cycle = False       # 싸이클인지 확인
    if visited[node]:   # 싸이클이다.
        return True
    visited[node] = 1  # 변호 했다.
    for next in graph[node]:
        if next == prev:  # 서로 변호하는거니까 안된다.
            continue
        if dfs(next, node):  # 연결된 노드를 보며 싸이클이 존재하는지 확인
            cycle = True
    return cycle



n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]  # i번째 변호사를 변호 했는가?

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)

interactive = []  # 서로 변호하는 사람들 담는다.
for i in range(1, n + 1):
    for v in graph[i]:
        if i not in graph[v]:  # 서로 변호 안하면
            visited[v] = 1     # i가 v를 변호하는걸로
        else:                  # 서로 변호하면
            if i > v:          # 하나만 담는다.(아니면 양 쪽 다 들어가서)
                interactive.append([i, v])

temp = [[] for _ in range(n + 1)]  # 양방향 연결된거만 남긴다.
for a, b in interactive:  # 양방향 연결된 노드들 확인하면서
    if visited[a] + visited[b] == 2:  # 둘 다 연결 안해도 되는 경우(다른 번호에게 변호를 받는 경우)
        continue
    elif visited[a] + visited[b] == 1:  # 둘중 하나가 0이다 > 양방향중에 하나를 연결할 수 있다.
        visited[a] = 1
        visited[b] = 1
    else:
        temp[a].append(b)
        temp[b].append(a)
graph = [temp[i][:] for i in range(n + 1)]  # 양방향인거만 남김

for i in range(1, n + 1):  # 사이클이 있는지 확인한다.
    if visited[i]:         # i가 변호를 받을 수 있다면
        continue
    if not graph[i] or not dfs(i, 0):  # 변호해줄 사람도 없는데, 변호해줄 사람도 없다. or 싸이클이 없다.
        print('NO')
        exit()
print('YES')
