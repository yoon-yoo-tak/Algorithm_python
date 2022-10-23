"""
20058 마법사 상어와 파이어스톰
rotated_arr=list(zip(*arr[::-1]))
"""
import sys
from collections import deque
input = sys.stdin.readline


def get_size(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1
    return cnt


def rotate(nums: int) -> None:
    ss = int(2 ** nums)
    for i in range(0, n, ss):
        for j in range(0, n, ss):
            # 담기
            temp = [[0] * ss for _ in range(ss)]
            for p in range(ss):
                for q in range(ss):
                    temp[p][q] = board[i + p][j + q]
            # 돌리기
            temp = list(zip(*temp[::-1]))
            # 넣기
            for p in range(ss):
                for q in range(ss):
                    board[i + p][j + q] = temp[p][q]
    erase(board)


def erase(ls):
    info = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                cnt = 0
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny]:
                        cnt += 1
                if cnt < 3:
                    info[x][y] = True
    for x in range(n):
        for y in range(n):
            if info[x][y]:
                board[x][y] -= 1


def calc(ls: list) -> int:
    total = 0
    for i in ls:
        total += sum(i)
    return total


N, _ = map(int, input().split())
n = int(2 ** N)
board = [list(map(int, input().split())) for _ in range(n)]
l = list(map(int, input().split()))
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * n for _ in range(n)]
# start
for Q in l:
    rotate(Q)

print(calc(board))
size = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and not visited[i][j]:
            size = max(size, get_size(i, j))
print(size)


