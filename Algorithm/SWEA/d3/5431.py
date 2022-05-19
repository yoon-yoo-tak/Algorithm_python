"""
5431 민석이의 과제 체크하기
"""
for tt in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    ls = [0] * (n + 1)
    lst = list(map(int, input().split()))
    for i in lst:
        ls[i] += 1
    print(f'#{tt}', end=' ')
    for i in range(1, len(ls)):
        if not ls[i]:
            print(i, end=' ')
    print()

