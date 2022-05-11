
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    minimum = int(1e9)
    n, m = map(int, input().split())
    ls = list(input().strip() for _ in range(n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            total = 0
            for k in range(m):
                total += abs(ord(ls[i][k]) - ord(ls[j][k]))
            minimum = min(minimum, total)
    print(minimum)

