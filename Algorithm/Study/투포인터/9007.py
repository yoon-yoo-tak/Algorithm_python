"""
9007 카누 선수
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(4)]
    a, b = set(), set()
    for i in range(0, 4, 2):
        for x in ls[i]:
            for y in ls[i+1]:
                a.add(x+y) if i == 0 else b.add(x+y)
    a = sorted(a)
    b = sorted(b)

    ans = 0
    differ = int(1e10)
    i, j = 0, len(b)-1
    while i < len(a) and 0 <= j:
        temp = a[i]+b[j]-k
        if abs(temp) < differ:
            differ = abs(temp)
            ans = temp + k
        elif abs(temp) == differ:
            ans = min(ans, temp+k)
        if temp < 0:
            i += 1
        elif temp > 0:
            j -= 1
        else:
            break

    print(ans)