"""
특정 구간의 원소 평균값
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i, n):
        if sum(ls[i:j + 1]) / (j - i + 1) in ls[i: j + 1]:
            ans += 1
print(ans)
