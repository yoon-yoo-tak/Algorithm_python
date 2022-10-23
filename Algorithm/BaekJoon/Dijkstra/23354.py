"""
23354 군탈체포조
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(sx, sy): # 다익
    dist = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, sx, sy))
    dist[sx][sy] = 0
    while q:
        dist_x, x, y = heapq.heappop(q)
        if dist_x != dist[x][y]:
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] > dist[x][y] + board[nx][ny]:
                dist[nx][ny] = dist[x][y] + board[nx][ny]
                heapq.heappush(q, (dist[nx][ny], nx, ny))
    return dist


def rec(k):  # 순열
    global ans
    if k == len(deserter):  # k개 뽑았다
        total = 0
        if len(selected) == 1:
            total += deserter_dist[0][start_x][start_y] * 2
        else:
            total += start_dist[deserter[selected[0]][0]][deserter[selected[0]][1]]  # 부대에서 처음 위치로 가는 최소비용
            for i in range(len(selected)):
                if i == len(selected) - 1:
                    total += deserter_dist[selected[-1]][start_x][start_y]  # 마지막위치에서 부대로 가는 최소비용
                else:
                    total += deserter_dist[selected[i]][deserter[selected[i + 1]][0]][deserter[selected[i + 1]][1]] # i번째에서 i+1번째로 가는 최소비용
        ans = min(ans, total)
    else:
        for i in range(len(deserter)):
            if not visited[i]:
                selected.append(i)
                visited[i] = True
                rec(k + 1)
                selected.pop()
                visited[i] = False


n = int(input())
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = INF
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            start_x, start_y = i, j  # 부대 위치

deserter = [(x, y) for y in range(n) for x in range(n) if board[x][y] == 0]  # 탈영병 위치들
board[start_x][start_y] = 0  # 부대 들렸다 가도 되니까 0으로
start_dist = dijkstra(start_x, start_y)
deserter_dist = [dijkstra(x, y) for x, y in deserter]

if len(deserter) == 0:  # 탈영병 없으면 0
    print(0)
    sys.exit()

selected = []
visited = [False] * (len(deserter))
rec(0)
print(ans)
