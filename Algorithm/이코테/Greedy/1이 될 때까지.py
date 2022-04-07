"""
이코테 그리디 파트 연습문제 - 1이 될 때까지

1. N에서 1을 뺀다.
2. N을 K로 나눈다.
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1
print(count)