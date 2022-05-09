import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 2, -1, -1):
        while a[i] >= a[i + 1] and a[i] > 0:
            a[i] //= 2
            ans += 1
        if a[i] >= a[i + 1]:
            ans = -1
            break
    print(ans)


