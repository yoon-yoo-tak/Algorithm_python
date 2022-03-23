"""

네트워크

"""
def solution(n, computers):
    visit = [[False] * n for _ in range(n)]
    dyx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    answer = 0
    def dfs(x, y):
        nonlocal answer
        visit[x][y] = True
        for dx, dy in dyx:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if computers[nx][ny] == 0:
                continue
            dfs(nx, ny)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0 or visit[i][j]:
                continue
            answer += 1
            dfs(i, j)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))