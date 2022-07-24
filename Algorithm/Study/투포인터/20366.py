"""
20366 같이 눈사라 만들래?
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))
ans = int(1e10)

for i in range(n):
    for j in range(i + 3, n):
        l, r = i + 1, j - 1
        while l <= r:
            total = (ls[i] + ls[j]) - (ls[l] + ls[r])
            ans = min(ans, abs(total))
            if total >= 0:
                l += 1
            else:
                r -= 1
print(ans)

