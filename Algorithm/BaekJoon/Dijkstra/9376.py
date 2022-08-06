"""
9376 탈옥
문이면 + 1 아니면 +0
"""
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 세명에 대한 다익스트라 돌리기
# 탈출위치가 문이면 세명의 탈출위치까지의 거리의 합 - 2(문은 한명만 따면 되니까)
# 문이 아니면 그 위치까지의 거리의 합


def dijkstra(x, y):
    q = []
    dist = [[INF] * (m + 2) for _ in range(n + 2)]
    heapq.heappush(q, [0, x, y])
    dist[x][y] = 0
    while q:
        distance, now_x, now_y = heapq.heappop(q)  # now_x, now_y 까지의 최단경로 distance
        if dist[now_x][now_y] != distance:
            continue
        for dx, dy in dxy:
            nx, ny = now_x + dx, now_y + dy # 다음 위치가
            if nx < 0 or nx >= n + 2 or ny < 0 or ny >= m + 2:  # 범위 벗어나면 무시
                continue
            if prison[nx][ny] == '*':  # 벽이면 무시
                continue
            if prison[nx][ny] == '#':  # 문이면 +1
                if dist[nx][ny] > dist[now_x][now_y] + 1:
                    dist[nx][ny] = dist[now_x][now_y] + 1
                    heapq.heappush(q, [dist[nx][ny], nx, ny])
            if prison[nx][ny] == '.' or prison[nx][ny] == '$':  # 땅이거나 죄수 위치면 +0
                if dist[nx][ny] > dist[now_x][now_y]:
                    dist[nx][ny] = dist[now_x][now_y]
                    heapq.heappush(q, [dist[nx][ny], nx, ny])
    return dist

for _ in range(int(input())):
    n, m = map(int, input().split())
    ls = [list(input().strip()) for _ in range(n)]

    # 밖에서 안으로 들어가는 최단경로 구하기 위해 감옥을 감싼다
    prison = [['.'] * (m + 2)]
    for i in range(n):
        temp = ['.'] + ls[i] + ['.']
        prison.append(temp)
    prison.append(['.'] * (m + 2))

    # 죄수 두명 좌표 저장
    aa = []
    for i in range(n + 2):
        for j in range(m + 2):
            if prison[i][j] == '$':
                aa.append([i, j])
    prisoner1 = aa[0]
    prisoner2 = aa[1]
    sg_dist = dijkstra(0, 0)  # 상근이가 밖에서 안으로 들어가는 최단경로
    p1_dist = dijkstra(aa[0][0], aa[0][1])  # 죄수 1이 안에서 밖으로 나가는 최단경로
    p2_dist = dijkstra(aa[1][0], aa[1][1])  # 죄수 2이 안에서 밖으로 나가는 최단경로
    tt = []
    door_cnt = int(1e5)
    for i in range(1, len(prison) - 1): # 테두리에서
        for j in range(1, len(prison[0]) - 1):
            if prison[i][j] == '#':  # 빠져나갈 수 있는 곳이 문이라면
                door_cnt = min(sg_dist[i][j] + p1_dist[i][j] + p2_dist[i][j] - 2, door_cnt)
            elif prison[i][j] == '.' or prison[i][j] == '$':  # 빠져나갈 수 있는 곳이 그냥 땅이면
                door_cnt = min(sg_dist[i][j] + p1_dist[i][j] + p2_dist[i][j], door_cnt)
    print(door_cnt)
