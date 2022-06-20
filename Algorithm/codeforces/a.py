"""

"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a, *b = map(int, input().split())
    cnt = 0
    for i in b:
        if i > a:
            cnt += 1
    print(cnt)