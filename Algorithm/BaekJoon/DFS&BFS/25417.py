"""
25417 고속의 숫자 탐색
"""
import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y):  # x, y 가 격자 내에 있는지
    return 0 <= x < 5 and 0 <= y < 5


def bfs():
    q = deque()
    q.append((start_x, start_y, 0))                     # 시작위치와 이동횟수 append
    visited[start_x][start_y] = True                    # 시작위치 방문 체크
    while q:
        x, y, cnt = q.popleft()                         # pop
        if board[x][y] == 1:                            # 목적지라면
            return cnt                                  # cnt return
        for dx, dy in dxy:                              # 뛰는 경우
            run_x, run_y = x, y
            while True:
                next_run_x, next_run_y = run_x + dx, run_y + dy
                if not in_range(next_run_x, next_run_y):# 다음 위치가 범위를 벗어나는 위치면 멈춤
                    break
                if board[next_run_x][next_run_y] == -1: # 다음 위치가 벽이면 멈춤
                    break
                if board[next_run_x][next_run_y] == 7:            # 7을 만나면 그자리에서 멈춘다
                    run_x, run_y = next_run_x, next_run_y
                    break
                run_x, run_y = next_run_x, next_run_y   # 셋다 아니면 계속 이동
            if visited[run_x][run_y]:                   # 뛰어왔는데 이미 방문한 곳이면 무시
                continue
            q.append((run_x, run_y, cnt + 1))           # append
            visited[run_x][run_y] = True                # 방문체크
        for dx, dy in dxy:                              # 걷는 경우
            nx, ny = x + dx, y + dy                     # 다음 위치가
            if not in_range(nx, ny):                    # 범위 벗어나면 무시
                continue
            if board[nx][ny] == -1:                     # 벽이면 무시
                continue
            if visited[nx][ny]:                         # 이미 방문한 곳이면 무시
                continue
            q.append((nx, ny, cnt + 1))                 # append
            visited[nx][ny] = True                      # 방문체크

    return -1                                           # 어떻게 해도 1에 도달할 수 없다 >> -1 return

board = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
start_x, start_y = map(int, input().split())
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

print(bfs())