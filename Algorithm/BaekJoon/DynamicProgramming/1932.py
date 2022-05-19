"""
1932 정수 삼각형
제일 왼쪽, 제일 오른쪽 숫자는 바로 윗 숫자와 더한다.
나머지는 위에 두개중에 큰거랑 더한다.
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
a = 2

for i in range(1, n):
    for j in range(a):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]
    a += 1
print(max(dp[n - 1]))