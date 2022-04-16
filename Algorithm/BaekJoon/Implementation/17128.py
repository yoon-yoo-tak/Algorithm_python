"""
17128 소가 정보섬에 올라온 이유
"""
import sys

input = sys.stdin.readline


N,Q = map(int,input().split())
A = list(map(int,input().split()))
dp = [0]*N

for i in range(N):
    dp[i] = A[i]*A[i-1]*A[i-2]*A[i-3]

Qs = list(map(int,input().split()))

ex_sum = sum(dp)
for idx in Qs:
    for i in range(4):
        new_idx = (idx-1+i)%N
        dp[new_idx] = -dp[new_idx]
        ex_sum += 2*dp[new_idx]
    print(ex_sum)
