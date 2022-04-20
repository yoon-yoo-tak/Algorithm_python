from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if grid[nx][ny] == '0':
                    continue
                if visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        return cnt
