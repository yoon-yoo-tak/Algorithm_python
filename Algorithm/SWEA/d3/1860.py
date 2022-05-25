"""
1860 진기의 최고급 붕어빵
"""
for tt in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    ls = sorted(map(int, input().split()))
    ans = 'Possible'
    for i in range(n):
        val = (ls[i] // m) * k - (i + 1)
        if val < 0:
            ans = 'Impossible'
            break
    print(f'#{tt} {ans}')
