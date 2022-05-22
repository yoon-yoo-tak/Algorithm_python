"""
원 모양으로 되어있는 방
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]

def calc(arr):
    total = 0
    for i in range(1, len(arr)):
        total += i * arr[i]
    return total
ans = int(1e9)
for i in range(n):
    ans = min(ans, calc(ls))
    ls.append(ls.pop(0))
print(ans)