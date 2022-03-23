"""

1337 올바른 배열

"""
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(int(input()) for _ in range(n))
b = []
for i in range(n):
    cnt = 0
    for j in range(a[i], a[i]+5):
        if j not in a:
            cnt += 1
    b.append(cnt)
print(min(b))