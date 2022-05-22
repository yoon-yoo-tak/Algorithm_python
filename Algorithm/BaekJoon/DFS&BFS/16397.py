"""
16397 탈출
"""
import sys
from collections import deque
input = sys.stdin.readline


def trans(num):
    if num == 0:
        return 0
    else:
        num *= 2
        num = list(str(num))
        num[0] = str(int(num[0]) - 1)
        num = int(''.join(num))
        return num

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        x = q.popleft()
        if x * 2 > 99999:
            nx = x + 1
            if nx < 0 or nx > 99999:
                continue
            if dist[nx] != -1:
                continue
            q.append(nx)
            dist[nx] = dist[x] + 1
        else:
            for nx in (x + 1, trans(x)):
                if nx < 0 or nx > 99999:
                    continue
                if dist[nx] != -1:
                    continue
                q.append(nx)
                dist[nx] = dist[x] + 1

n, t, g = map(int, input().split())
dist = [-1] * 1000000
bfs(n)
if dist[g] > t or dist[g] == -1:
    ans = 'ANG'
else:
    ans = dist[g]
print(ans)
