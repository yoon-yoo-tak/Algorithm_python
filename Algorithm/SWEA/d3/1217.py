"""
1217 거듭 제곱
"""
def rec(n, m):
    if m == 0:
        return 1
    return n * rec(n, m - 1)


for i in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    print(f'#{t} {rec(n, m)}')


