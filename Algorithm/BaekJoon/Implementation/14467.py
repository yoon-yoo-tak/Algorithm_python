"""
14467 소가 길은 건너간 이유 1
"""
import sys

input = sys.stdin.readline
n = int(input())
ls = [[] for _ in range(11)]
for _ in range(n):
    a, b = map(int, input().split())
    ls[a].append(b)
cnt = 0
for i in ls:
    if len(i) >= 2:
        for j in range(len(i) - 1):
            if i[j] != i[j + 1]:
                cnt += 1
    else:
        continue

print(cnt)