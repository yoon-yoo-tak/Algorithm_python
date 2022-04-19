from collections import deque
def solution(maps):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if dist[nx][ny] != -1:
                continue
            if maps[nx][ny] == 0:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    for i in dist:
        print(i)
    return dist[len(maps) - 1][len(maps[0]) - 1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
