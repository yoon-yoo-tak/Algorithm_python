"""
프로그래머스 레벨 2 배달

"""
import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    dist = [int(1e9)] * (N + 1)
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] != dist_x:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))
    for i in dist[1:]:
        if i <= K:
            answer += 1

    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))