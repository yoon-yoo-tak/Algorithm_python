"""
첫 번째 줄에 a에서 b사이 소수이면서 모든 자리수의 합이 짝수인 수의 개수를 출력합니다.
"""

import sys

input = sys.stdin.readline

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_even(n):
    total = 0
    for i in str(n):
        total += int(i)
    if total % 2 == 0:
        return True
    else:
        return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if is_prime(i) and is_even(i):
       cnt += 1

print(cnt)