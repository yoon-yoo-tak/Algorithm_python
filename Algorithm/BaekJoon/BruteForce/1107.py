"""
1107 리모컨
100번 에서 출발
채널 무한대
"""
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
    ls = list(map(int, input().split()))
else:
    ls = []
maxi = abs(n - 100)

for i in range(1000001):
    for j in str(i):
        if int(j) in ls:
            break
    else:
        maxi = min(maxi, abs(i - n) + len(str(i)))
print(maxi)