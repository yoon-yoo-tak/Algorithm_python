"""
15683 감시
"""

import sys
import copy
input = sys.stdin.readline
INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[],
             [[0], [1], [2], [3]],  # 1번 cctv
             [[0, 1], [2, 3]],      # 2번 cctv
             [[0, 2], [2, 1], [1, 3], [3, 0]],  # 3번 cctv
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]  # 4번 cctv
             ]

def watch(y, x, direction, tmp):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                break

def dfs(office, cnt):
    global ans

    tmp = copy.deepcopy(office)
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    y, x, cctv = q[cnt]
    for i in direction[cctv]:
        watch(y, x, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)

n, m = map(int, input().split())
office = []
cctv_cnt = 0
q = []
ans = INF
for i in range(n):
    ls = list(map(int, input().split()))
    office.append(ls)
    for j in range(m):
        if ls[j] != 0 and ls[j] != 6:
            cctv_cnt += 1
            q.append([i, j, ls[j]])

dfs(office, 0)
print(ans)