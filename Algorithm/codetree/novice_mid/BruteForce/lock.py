"""
한가지로 열리는 자물쇠
"""
import sys

input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(a - i) <= 2 or abs(b - j) <= 2 or abs(c - k) <= 2:
                cnt += 1
print(cnt)