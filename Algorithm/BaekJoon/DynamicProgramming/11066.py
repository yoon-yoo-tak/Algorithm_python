"""
11066 파일 합치기
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ls = [0] + list(map(int, input().split()))

    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i, n + 1):
            prefix_sum[i][j] = prefix_sum[i][j - 1] + ls[j]

    for i in range(2, n + 1):
        for j in range(1, n - i + 2):
            k = j + i - 1
            dp[j][k] = 500 * 500 * int(1e4)
            for x in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][x] + dp[x + 1][k] + prefix_sum[j][k])
    print(dp[1][n])
