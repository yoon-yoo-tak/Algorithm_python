import sys

input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]
cnt, ans = 0, 0
for i in range(n):
    if i >= 1 and ls[i] * ls[i - 1] > 0:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)