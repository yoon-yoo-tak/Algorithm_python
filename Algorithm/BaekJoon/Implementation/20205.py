"""

20205 교수님 그림이 깨지는데요

"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for s in range(k):
        for j in range(n):
            for l in range(k):
                print(ls[i][j], end=' ')
        print()
