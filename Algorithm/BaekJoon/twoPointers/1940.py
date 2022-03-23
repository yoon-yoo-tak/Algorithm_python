"""

1940 주몽

"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = sorted(map(int, input().split()))

start, end = 0, n - 1
cnt = 0
while start < end:
    if a[start] + a[end] == m:
        cnt += 1
        start += 1
        end -= 1
    elif a[start] + a[end] < m:
        start += 1
    else:
        end -= 1
print(cnt)
