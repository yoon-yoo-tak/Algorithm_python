#  네이버 공채 3번

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for __ in range(n)]


def move(x, y, d):
    if d == 0: return (x - 1, y)
    if d == 1:
        if y % 2 == 0:
            return (x - 1, y + 1)
        else:
            return (x, y + 1)
    if d == 2:
        if y % 2 == 0:
            return (x, y + 1)
        else:
            return (x + 1, y + 1)
    if d == 3: return (x + 1, y)
    if d == 4:
        if y % 2 == 0:
            return (x, y - 1)
        else:
            return (x + 1, y - 1)
    if d == 5:
        if y % 2 == 0:
            return (x - 1, y - 1)
        else:
            return (x, y - 1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def coloring(start, goal):
    for d in range(6):
        flag = False
        p = start
        while in_range(p[0], p[1]):
            p = move(p[0], p[1], d)
            if p == goal:
                flag = True
                break

        if flag:
            p = start
            while p != goal:
                p = move(p[0], p[1], d)
                visit[p[0]][p[1]] = 1
            break


cnt = int(input())
points = [tuple(map(int, input().split())) for _ in range(cnt)]
points.append(points[0])
for i in range(cnt):
    cur = points[i]
    nxt = points[i + 1]
    coloring(cur, nxt)
ans = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1: continue
        flag = 0
        for d in range(6):
            ni, nj = move(i, j, d)
            if in_range(ni, nj) and visit[ni][nj] == 1: flag = 1
        if flag == 1:
            ans += a[i][j]

print(ans)