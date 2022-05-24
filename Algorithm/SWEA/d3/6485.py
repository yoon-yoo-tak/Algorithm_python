"""
6485 삼성시의 버스 노선
"""
for tt in range(1, int(input()) + 1):
    n = int(input())
    bus = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    ans = [0] * p
    for i in range(p):
        c = int(input())
        for x, y in bus:
            if x <= c <= y:
                ans[i] += 1
    print(f'#{tt}', end=' ')
    print(*ans)
