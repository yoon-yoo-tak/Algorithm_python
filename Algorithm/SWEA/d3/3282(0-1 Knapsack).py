"""
3282 0-1 Knapsack
"""
t = int(input())
ls = []
for tt in range(t):
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]
    ls.append((n, k, item))

ans = []

for tt in range(t):
    n, k, item = ls[tt]
    dp = [[0] * (k + 1) for _ in range(1 + n)]

    for i in range(1, len(dp)):
        v, c = item[i - 1]
        for j in range(1, len(dp[i])):
            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]
    ans.append(dp[-1][-1])

for tt in range(t):
    print(f'#{tt + 1} {ans[tt]}')