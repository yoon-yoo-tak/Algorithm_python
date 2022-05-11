import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ls = sorted(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        cnt += ls[i] - ls[0]
    print(cnt)

