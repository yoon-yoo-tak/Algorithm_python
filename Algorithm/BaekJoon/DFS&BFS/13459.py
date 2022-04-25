"""
13459 구슬탈출
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()


def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            if graph[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    cnt = 0  # 구슬의 이동거리를 저장할 변수
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':  # 벽을 만나거나 구멍에 빠질 때 까지 한쪽 방향으로 계속 이동.
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:  # 10번 이내에 구멍으로 못빠져나가면
            break       # 종료
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # 구슬들을 각 방향마다 이동시켜본다.
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if graph[nbx][nby] != 'O':  # 파란구슬이 구멍에 빠지지 않았고
                if graph[nrx][nry] == 'O':  # 빨간 구슬이 구멍에 빠졌다면 종료
                    print(1)
                    return
                if nrx == nbx and nry == nby:  # 빨간구슬이랑 파란구슬이 같은 위치에 있고
                    if rcnt > bcnt:            # 빨간구슬이 움직인 거리가 더 크면
                        nrx -= dx[i]           # 빨간 구슬의 위치를 1칸 되돌린다
                        nry -= dy[i]
                    else:                      # 파란구슬이 움직인 거리가 더 크면
                        nbx -= dx[i]           # 파란 구슬의 위치를 1칸 되돌린다
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:  # 움직인 위치가 처음 방문한 위치이면
                    visited[nrx][nry][nbx][nby] = True  # 방문처리 하고
                    q.append((nrx, nry, nbx, nby, depth + 1))  # 큐에 구슬들이 움직인 좌표와 움직인횟수 + 1 을 넣어준다
    print(0)

bfs()