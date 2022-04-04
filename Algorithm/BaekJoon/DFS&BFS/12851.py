"""
12851 숨바꼭질 2

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
maxDist = 100000
dist = [-1] * (maxDist + 1)
method = [0] * (maxDist + 1)
def bfs(x):
    q = deque()
    q.append(x)
    dist[x] = 0
    method[x] = 1
    while q:
        x = q.popleft()
        for nx in [x + 1, x - 1, x * 2]:
            if 0 <= nx <= maxDist:  # 다음 위치가 범위 안에 있다면
                if dist[nx] == -1:  # 다음 위치를 처음 본다면
                    dist[nx] = dist[x] + 1  # 이전 위치의 거리 +1
                    method[nx] = method[x]  # 이전 위치까지 오는 방법에서 오는것이므로 같은 가짓수
                    q.append(nx)
                else:  # 다음위치가 처음 본 것이 아니고,
                    if dist[nx] == dist[x] + 1:  # 다음위치까지의 거리가 현재 위치에서 +1 한 값이랑 같다면 (이전 방법이 아닌 다른 방법으로 접근한것이다)
                        method[nx] += method[x]  # 다음 위치에 도달할 수 있는 가짓수 + 현재 위치까지 도달할 수 있는 가짓수

bfs(n)
print(dist[k])
print(method[:k + 1])
print(method[k])