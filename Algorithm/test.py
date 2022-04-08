import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
cream = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    cream[a - 1][b - 1] = True
    cream[b - 1][a - 1] = True

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not cream[i][j] and not cream[i][k] and not cream[j][k]:
                ans += 1

print(ans)

