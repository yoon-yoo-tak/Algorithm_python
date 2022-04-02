"""
2011 암호코드

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

a = input().strip()
n = len(a)

def check(A: chr, B: chr): #AB가 처리 가능한 숫자인지
    if A == '0': return False # 03 02 등의 숫자는 처리하지마라.
    if A == '1': return True # 10 ~ 19는 처리가능해서 True
    if A >= '3': return False # 알파벳 26개라 3으로시작하는 두자리 숫자는 pass
    return B <= '6' # 26까지이기때문에 16, 26 처리하기 위해


dp = [0] * n

if a[0] != '0':
    dp[0] = 1

for i in range(1, n):
    # 0이면 10, 20 으로 봐야한다.
    if a[i] != '0':
        # 한자리로 보면 바로 앞 자리까지 해석한것에 하나만 추가되는것이므로
        dp[i] = dp[i - 1]

    if check(a[i - 1], a[i]):
        if i >= 2: dp[i] += dp[i - 2]
        else:
            dp[i] += 1
        dp[i] %= 1000000

print(dp[n - 1])