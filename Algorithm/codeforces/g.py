"""

"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    ls = list(map(int ,input().split()))
    cnt = 0
    for i in range(n - k):
        for j in range(i, i + k):
            if ls[j] >= 2 * ls[j + 1]:
                break
        else:
            cnt += 1
    print(cnt)
