"""

8979 올림픽

1. 금메달 수가 더 많은 나라
2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

"""
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if s[i][0] == k:
        index = i
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break