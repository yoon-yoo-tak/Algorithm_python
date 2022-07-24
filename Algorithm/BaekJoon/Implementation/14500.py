"""
14500 테트로미노
ㅡ ㄴ ㅜ ㅁ ㄹ
"""
import sys

input = sys.stdin.readline


def dfs(x, y, index, total):
    global ans
    if ans >= total + big * (3 - index):
        return
    if index == 3:
        ans = max(ans, total)
        return
    else:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if index == 1:
                visited[nx][ny] = True
                dfs(x, y, index + 1, total + ls[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, index + 1, total + ls[nx][ny])
            visited[nx][ny] = False


n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
big = max(map(max, ls))
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * m for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, ls[i][j])
        visited[i][j] = False

print(ans)
