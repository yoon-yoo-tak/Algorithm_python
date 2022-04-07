"""
이코테 챕터 11(그리디) 1번. 모험가 길드

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
input = sys.stdin.readline
n = int(input())
ls = sorted(map(int, input().split()))

ans = 0
count = 0
for i in ls:
    count += 1
    if count >= i:
        ans += 1
        count = 0

print(ans)
