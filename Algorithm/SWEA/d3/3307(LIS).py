"""
3307 최장 증가 부분 수열
"""
for tt in range(1, int(input()) + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if ls[i] > ls[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{tt} {max(dp)}')
