"""
M개의 구간으로 선택하기
"""
NUM_STATE = 2
MIN_ANS = -500000

NOT_BELONG = 0
BELONG = 1

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = [0 for _ in range(n + 1)]

dp = [[[0 for i in range(NUM_STATE + 1)]for _ in range(m + 1)]for _ in range(n + 1)]


def initialize():
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            dp[i][j][NOT_BELONG] = dp[i][j][BELONG] = MIN_ANS

    for i in range(0, n + 1):
        dp[i][0][NOT_BELONG] = 0


given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

for i in range(1, n + 1):
    for j in range(1, m + 1):

        dp[i][j][BELONG] = max(dp[i - 1][j - 1][NOT_BELONG] + a[i], dp[i - 1][j][BELONG] + a[i])

        dp[i][j][NOT_BELONG] = max(dp[i - 1][j][NOT_BELONG], dp[i - 1][j][BELONG])

print(max(dp[n][m][NOT_BELONG], dp[n][m][BELONG]))