"""
4108 지뢰찾기
"""
import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ls = [list(input().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ls[i][j] == '.':
                ls[i][j] = 0
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(n):
        for j in range(m):
            if ls[i][j] == 0:
                for dx, dy in dxy:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == '*':
                        ls[i][j] += 1
    for i in range(n):
        for j in range(m):
            print(ls[i][j], end='')
        print()