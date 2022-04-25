"""
3048 개미

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s1 = list(input().strip()[::-1])
s2 = list(input().strip())
t = int(input())
dir = {}
for i in s1:
    dir[i] = 0
for i in s2:
    dir[i] = 1
s1 += s2
for _ in range(t):
    cnt = 0
    while cnt < len(s1) - 1:
        if dir[s1[cnt]] == 0 and dir[s1[cnt + 1]] == 1:
            s1[cnt], s1[cnt + 1] = s1[cnt + 1], s1[cnt]
            cnt += 1
        cnt += 1
print(''.join(s1))




