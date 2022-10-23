"""
1486 등산
높이차이가 t보다 작거나 같은곳만 이동 가능
D보다 작거나 같은 시간 안에 이동 가능한 최대 높이
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e8)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


n, m, t, d = map(int, input().split())
mountain = [list(input().strip()) for _ in range(n)]

# 높이로 다 바꿔줌
for i in range(n):
    for j in range(m):
        if 65 <= ord(mountain[i][j]) <= 90:
            mountain[i][j] = ord(mountain[i][j]) - 65           # A ~ Z > 0 ~ 25
        else:
            mountain[i][j] = ord(mountain[i][j]) - 71           # a ~ z > 26 ~ 51


# 다익스트라
q = []
dist = [[INF] * m for _ in range(n)]
heapq.heappush(q, (0, 0, 0))
dist[0][0] = 0

while q:
    dist_x, x, y = heapq.heappop(q)
    if dist_x != dist[x][y]:
        continue
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:              # not in range
            continue
        if abs(mountain[x][y] - mountain[nx][ny]) > t:          # 높이차이가 t보다 크면 못간다
            continue
        if mountain[x][y] >= mountain[nx][ny]:                  # 높이가 같거나 작은 곳이면 1초가 걸린다.
            if dist[nx][ny] > dist[x][y] + 1:                   # 더 적게 걸리면
                dist[nx][ny] = dist[x][y] + 1                   # 갱신
                heapq.heappush(q, (dist[nx][ny], nx, ny))       # push
        else:                                                   # 높으면 차이의 제곱만큼 걸린다.
            time = int((mountain[x][y] - mountain[nx][ny]) ** 2)
            if dist[nx][ny] > dist[x][y] + time:                # 더 적게 걸리면
                dist[nx][ny] = dist[x][y] + time                # 갱신
                heapq.heappush(q, (dist[nx][ny], nx, ny))       # push
ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] <= d:                                     # d시간 안에 갈 수 잇는곳이면
            ans = max(ans, mountain[i][j])                      # 정답 갱신

print('산 높이')
for i in mountain:
    print(*i)
print('걸리는 시간')
for i in dist:
    print(*i)
print(ans)
