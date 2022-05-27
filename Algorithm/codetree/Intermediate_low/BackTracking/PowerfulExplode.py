"""
강력한 폭발
"""
import sys

input = sys.stdin.readline


def one_explode(x, y): # 1번 폭탄
    dxy = [(1, 0), (2, 0), (-1, 0), (-2, 0)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        board[nx][ny] = 1


def two_explode(x, y):  # 2번 폭탄
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        board[nx][ny] = 1


def three_explode(x, y):  # 3번 폭탄
    dxy = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        board[nx][ny] = 1


def check():  # 총 폭발 범위 리턴
    cnt = 0
    for i in board:
        cnt += i.count(1)
    return cnt


def explode(selected, position): # 선택된 폭탄번호에 대해 폭발시키기
    global board
    for i in range(len(selected)):
        if selected[i] == 1:
            one_explode(position[i][0], position[i][1])
        elif selected[i] == 2:
            two_explode(position[i][0], position[i][1])
        else:
            three_explode(position[i][0], position[i][1])
    temp = check()
    board = [[0] * n for _ in range(n)]
    for x, y in one_pos:
        board[x][y] = 1
    return temp


# (1, 2, 3)에서 중복하여 bomb_cnt개 뽑아서 폭발시켜보고 총 폭발구역 갱신
def rec(k):
    global ans
    if k == bomb_cnt:  # k개 뽑았으면
        ans = max(ans, explode(sel, one_pos))  # 폭발시키고 정답 갱신
    else:
        for i in range(1, 4):  # (1, 2, 3) 을 중복을 허용해서 bomb_cnt개 뽑기
            sel.append(i)
            rec(k + 1)
            sel.pop()


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 폭탄을 놓을 수 있는 좌표 저장
one_pos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            one_pos.append([i, j])
bomb_cnt = len(one_pos)
sel = []
ans = 0
rec(0)
print(ans)