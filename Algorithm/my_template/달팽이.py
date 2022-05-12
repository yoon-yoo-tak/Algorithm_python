"""
2차원 달팽이배열 // 나선형 번호 매기기
n * n 배열에서 달팽이 배열 만들기
"""
n = int(input())
snail = [[0] * n for _ in range(n)]

# 방향만 필요에 따라 바꿔서 사용하기
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, d, v = 0, 0, 0, n * n

while True:
    if v == 0:
        break
    snail[x][y] = v
    nx, ny = x + dx[d], y + dy[d]
    v -= 1
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        d = (d + 1) % 4
        x, y = x + dx[d], y + dy[d]
        continue
    if snail[nx][ny] != 0:
        d = (d + 1) % 4
        x, y = x + dx[d], y + dy[d]
        continue
    x, y = nx, ny


for i in snail:
    print(i)
