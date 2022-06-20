"""
우리는 하나
"""
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
selected_city = []
city_pos = []

q = deque()

ans = 0

for i in range(n):
    for j in range(n):
        city_pos.append((i, j))


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, curr_city):
    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False

    differece_high = abs(curr_city - grid[x][y])
    if u > differece_high or d < differece_high:
        return False

    return True


def bfs():
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, grid[x][y]):
                visited[nx][ny] = True
                q.append((nx, ny))


def calc():
    for x, y in selected_city:
        q.append((x, y))
        visited[x][y] = True

    # print(q)

    bfs()

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    return cnt


def max_find(idx, cnt):
    global ans

    if cnt > k:
        return

    if idx == len(city_pos):
        if cnt == k:
            ans = max(ans, calc())
        return

    selected_city.append(city_pos[idx])
    max_find(idx + 1, cnt + 1)
    selected_city.pop()

    max_find(idx + 1, cnt)


max_find(0, 0)
print(ans)
