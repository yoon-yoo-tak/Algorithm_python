"""
1981 배열에서의 이동
"""
import sys
from collections import deque
input = sys.stdin.readline

def ok(midd):
    q = deque()
    for i in range(min_val, max_val + 1):
        visited = [[True] * n for _ in range(n)]
        for j in range(n):
            for k in range(n):
                if i <= ls[j][k] <= i + midd:
                    visited[j][k] = False
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n -1 and y == n - 1:
                return True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                q.append((nx, ny))
    return False



n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min_val, max_val = 201, -1
for i in ls:
    min_val = min(min_val, min(i))
    max_val = max(max_val, max(i))

l, r = 0, max_val - min_val
ans = r
while l <= r:
    mid = (l + r) // 2
    if ok(mid):  # 이동가능하면 범위줄여본다.
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)