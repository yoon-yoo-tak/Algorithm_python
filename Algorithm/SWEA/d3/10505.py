"""
10505 소득 불균형
"""
t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    avg = sum(ls) / n
    cnt = 0
    for i in ls:
        if i <= avg:
            cnt += 1
    print(f'#{tt} {cnt}')