"""
일렬로 서있는 소 2
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if ls[i] <= ls[j] <= ls[k]:
                cnt += 1

print(cnt)