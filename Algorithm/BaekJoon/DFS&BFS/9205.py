"""
9205 맥주 마시면서 걸어가기
"""
import sys
from collections import deque

input = sys.stdin.readline


def can_go(sx, sy, ex, ey):  # (sx, sy)에서 (ex, ey) 를 갈 수 있는가?
    return abs(sx - ex) + abs(sy - ey) <= 1000


def bfs():
    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        if can_go(x, y, end_x, end_y):  # 현재 위치에서 도착지까지 갈 수 있다면
            return 'happy'
        for i in range(n):
            if not vis[i]:  # i번째 편의점을 아직 안갔다면
                nx, ny = store[i]  # i 번째 편의점 위치에 대해서
                if can_go(x, y, nx, ny):  # 현재 위치에서 갈 수 있다면
                    q.append((nx, ny))  # 큐에 넣는다.
                    vis[i] = True  # 방문처리
    return 'sad'  # 어떻게 해도 도달하지 못했을 경우


t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())  # 시작위치 입력
    store = [list(map(int, input().split())) for _ in range(n)]  # 편의점 위치들
    end_x, end_y = map(int, input().split())  # 도착위치
    vis = [False] * (n + 1)  # 방문 배열
    print(bfs())
