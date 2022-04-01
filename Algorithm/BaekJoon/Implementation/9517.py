"""
9517 아이 러브 크로아티아

1. 아이디어
2. 시간복잡도
3. 자료구조
"""
import sys
input = sys.stdin.readline
k = int(input())
n = int(input())
time = 0
for i in range(n):
    a, b = input().split()
    time += int(a)
    if time >= 210:
        print(k)
        break
    if b == 'T':
        k = (k + 1) % 9
        if k == 0:
            k += 1



