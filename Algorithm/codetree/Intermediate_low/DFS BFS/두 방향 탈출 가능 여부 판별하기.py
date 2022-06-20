"""
두 방향 탈출 가능 여부 판별하기
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or graph[x][y] == 0:
        return False
    return True

def dfs(x, y):
    visited[x][y] = 1
    dxy = [(1, 0), (0, 1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

dfs(0, 0)
print(visited[n - 1][m - 1])
