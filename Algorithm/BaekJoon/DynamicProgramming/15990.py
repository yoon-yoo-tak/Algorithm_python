"""
15990 1, 2, 3 더하기 5

"""
import sys
MOD = 1000000009
input = sys.stdin.readline

dp = [[0] * 4 for _ in range(100005)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 100001):
    for now in range(1, 4):
        for before in range(1, 4):
            if now == before:
                continue
            dp[i][now] += dp[i - now][before]
            dp[i][now] %= MOD

for _ in range(int(input())):
    print(sum(dp[int(input())]) % MOD)

