"""
11445 무한 사전
"""
import sys

input = sys.stdin.readline
for t in range(int(input())):
    p = input().strip()
    q = input().strip()

    if p + 'a' == q:
        result = 'Y'
    else:
        result = 'N'
    print(f'#{t + 1} {result}')