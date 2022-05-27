"""
1차원 젠가
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [0] + list(int(input()) for _ in range(n))
for _ in range(2):
    s, e = map(int, input().split())
    s -= 1
    for i in range(s, e):
        ls[i] = 0
    last = 0
    for i in range(1, len(ls)):
        if ls[i] == 0:
            continue
        last += 1
        ls[last] = ls[i]
    for i in range(last + 1, len(ls)):
        ls[i] = 0
cnt = len([i for i in ls if i != 0])
print(cnt)
for i in ls:
    if i != 0:
        print(i)



