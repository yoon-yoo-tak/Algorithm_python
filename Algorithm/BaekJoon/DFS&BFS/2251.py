"""

2251 물통

정점 : 상태
간선 : 다른 상태로 간다.

"""
import sys
from collections import deque
input = sys.stdin.readline

limit = map(int, input().split())

visit = [[[False] * 205 for _ in range(205)] for _ in range(205)]
poss = [0] * 205


def bfs():
    def move(cur, f, t):
        res = [cur[0], cur[1], cur[2]]
        if cur[f] + cur[t] <= limit[t]:
            res[t] = res[f] + res[t]
            res[f] = 0
        else:
            res[f] -= limit[t] - res[t]
            res[t] = limit[t]
        return res

    q = deque()
    q.append([0, 0, limit[2]])
    visit[0][0][limit[2]] = True

    while q:
        cur = q.popleft()
        if cur[0] == 0: poss[cur[2]] = True
        for f in range(3):
            for t in range(3):
                if f == t: continue
                nxt = move(cur, f, t)
                if visit[nxt[0]][nxt[1]][nxt[2]]:continue
                visit[nxt[0]][nxt[1]][nxt[2]] = True
                q.append(nxt)


bfs()
for i in range(205):
    if poss[i]:
        print(i, end=' ')