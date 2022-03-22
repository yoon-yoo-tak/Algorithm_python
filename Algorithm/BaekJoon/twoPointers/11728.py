"""

11728 배열 합치기


"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

L, R = 0, 0
while L < n and R < m:
    if a[L] <= b[R]:
        print(a[L], end=' ')
        L += 1
    else:
        print(b[R], end=' ')
        R += 1
while L < n:
    print(a[L], end=' ')
    L += 1
while R < m:
    print(b[R], end=' ')
    R += 1



