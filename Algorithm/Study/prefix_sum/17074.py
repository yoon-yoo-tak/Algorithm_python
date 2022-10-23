"""
17074 정렬
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [-int(1e9)] + list(map(int, input().split())) + [int(1e9)]
idx = ans = cnt = 0
for i in range(2, n + 2):
    if ls[i] < ls[i - 1]:
        cnt += 1
        idx = i
if cnt == 0: # 정렬 되어 있다면
    ans = n
elif cnt == 1:
    if ls[idx - 1] <= ls[idx + 1]:
        ans += 1
    if ls[idx - 2] <= ls[idx]:
        ans += 1
print(ans)


