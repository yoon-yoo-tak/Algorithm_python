"""
5046 전국 대학생 프로그래밍 대회 동아리 연합

"""

import sys

input = sys.stdin.readline

n, b, h, w = map(int, input().split())
total_price = int(1e9)
for _ in range(h):
    p = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i >= n:
            total_price = min(total_price, p * n)

print(total_price if total_price < b else 'stay home')

