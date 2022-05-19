"""
5789 현주의 상자 바꾸기
"""
for t in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    ls = [0] * n
    for qq in range(1, q + 1):
        a, b = map(int, input().split())
        for i in range(a - 1, b):
            ls[i] = qq
    print(f'#{t}', end=' ')
    print(*ls)