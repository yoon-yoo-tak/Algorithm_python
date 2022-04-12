"""
성적이 낮은 순서로 학생 출력하기

"""

import sys

input = sys.stdin.readline
n = int(input())
ls = []
for _ in range(n):
    a, b = input().split()
    ls.append((a, int(b)))
ls.sort(key=lambda x:x[1])
for i, j in ls:
    print(i, end=' ')