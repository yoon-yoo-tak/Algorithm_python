"""
이상한 진수 2
"""
import sys

input = sys.stdin.readline

int_min = -sys.maxsize

bi = list(map(int, list(input().strip())))
le = len(bi)

ans = int_min

for i in range(le):
    bi[i] = 1 - bi[i]
    num = 0
    for j in range(le):
        num = num * 2 + bi[j]
    ans = max(ans, num)

    bi[i] = 1 - bi[i]

print(ans)


