"""
10851 숫자 카드
"""
import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
q = int(input())
qq = list(map(int, input().split()))

for i in qq:
    ans = 0
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if ls[mid] == i:
            answer = 1
            break
        elif ls[mid] < i:
            l = mid + 1
        else:
            r = mid - 1
    print(ans, end= ' ')