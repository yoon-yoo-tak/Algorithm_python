"""

18290 NM 과 K(1)

N X M 의 격자판에서 K개 선택해서 합이 최대가 되는 경우 출력

인접한 칸 선택 불가

"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dyx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
sel = []
answer = -1000000
def rec(cx, cy, idx, sum):
    if idx == k:
        global answer
        if answer < sum:
            answer = sum
        return
    for x in range(cx, n):
        for y in range(cy if x == cx else 0, m):
            if visited[x][y]:
                continue

            ok = True
            for dx, dy in dyx:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n  and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False
            if ok:
                visited[x][y] = True
                rec(x, y, idx + 1, sum+a[x][y])
                visited[x][y] = False

rec(0, 0, 0, 0)
print(answer)
