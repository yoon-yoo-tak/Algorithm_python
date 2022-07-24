"""
16985 Maaaaaaaaaze
판 5개를 배치하는 방법.
배치했을 때 각각 돌려보는 방법.(순열?) > (0, 0, 0, 0, 0) , (0, 0, 0, 0, 1), (0 ,0 ,0, 0, 2) .... (3, 3, 3, 3, 3)
"""
import sys
from collections import deque

input = sys.stdin.readline


def rotate_90(a): # 90도 회전
    row_length = len(a)
    col_length = len(a[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = a[r][c]
    return res

def bfs(ls):
    q = deque()
    dist = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    start_end_point = []
    for i in [0, 4]:
        for j in [0, 4]:
            for k in [0, 4]:
                start_end_point.append([i, j, k])
    for z, x, y in start_end_point[:4]:
        q.append([z, x, y])
        dist[z][x][y] = 0
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if nz < 0 or nz >= 5 or nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if dist[nz][nx][ny] != -1:
                continue
            if not ls[nz][nx][ny]:
                continue
            q.append((nz, nx, ny))
            dist[nz][nx][ny] = dist[z][x][y] + 1
    answer = []
    for z, x, y in start_end_point[4:]:
        if dist[z][x][y] != -1:
            answer.append(dist[z][x][y])
    if len(answer) == 0:
        return 400
    return min(answer)


def rotate_maze(ls: list):
    for i in range(5):
        temp = selected[i]
        for j in range(ls[i]):
            temp = rotate_90(temp)
    return temp


def make(k):
    global ans
    if k == 5:
        rotated = rotate_maze(make_selected)
        ans = min(ans, bfs(rotated))
    else:
        for i in range(5):
            make_selected.append(i)
            make(k + 1)
            make_selected.pop()


def pick(k):  # 판 순서 고르기
    if k == 5:  # 다 뽑았다 ! # 뽑았으니까? 뽑은걸로? 다시 돌려보는 경우의 수 돌려서? bfs 돌려서? 거리 갱신
        pass
    else:
        for i in range(5):
            if not visited[i]:
                selected.append(maze[i])
                visited[i] = True
                pick(k + 1)
                selected.pop()
                visited[i] = False


maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

visited = [False] * 5
selected = []
make_selected = []
ans = 400
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
pick(0)
print(-1 if ans == 400 else ans)