"""
13717 포켓몬
"""
import sys

input = sys.stdin.readline

n = int(input())
res = 0
ans = 0
name = ''

for _ in range(n):
    poket_mon = input()
    k, m = map(int, input().split())

    cnt = 0

    while m >= k:
        m -= k
        m += 2
        cnt += 1

    # result.append(cnt)
    res += cnt
    if ans < cnt:
        ans = cnt
        name = poket_mon

print(res)
print(name)