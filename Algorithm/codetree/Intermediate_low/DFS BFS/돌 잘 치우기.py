"""
돌 잘 치우기
k개의 시작점 q에넣기
전체 돌의 갯수중에 m개 치우고 탐색. 반복 > 최댓값 갱신
함수
범위확인
뽑기
탐색
"""
import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if board[x][y] == 1:
        return False
    return True

def bfs():
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    for x, y in start:
        q.append((x, y))
        dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    temp = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1:
                temp += 1
    return temp


def rec(x, cnt):
    global total_stone, ans
    if x == total_stone:
        if cnt == m:
            for x, y in selected:
                board[x][y] = 0
            ans = max(ans, bfs())
            for x, y in selected:
                board[x][y] = 1
    else:
        selected.append(stone[x])
        rec(x + 1, cnt + 1)
        selected.pop()
        rec(x + 1, cnt)



n, k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = -1
start = []
for _ in range(k):
    x, y = map(lambda x: x - 1, map(int, input().split()))
    start.append((x, y))

stone = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            stone.append((i, j))
total_stone = len(stone)
# total_stone 개에서 m개 뽑기

selected = []
rec(0, 0)
print(ans)




