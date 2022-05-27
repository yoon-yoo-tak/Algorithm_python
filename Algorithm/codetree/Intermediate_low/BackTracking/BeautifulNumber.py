"""
아름다운 수
"""
import sys

input = sys.stdin.readline

n = int(input())
ans = 0
seq = list()

def is_beautiful():
    i = 0
    while i < n:
        if i + seq[i] - 1 >= n:
            return False

        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
        i += seq[i]
    return True

def count(cnt):
    global ans
    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    for i in range(1, 5):
        seq.append(i)
        count(cnt + 1)
        seq.pop()

count(0)
print(ans)


# dp 풀이

# n = int(input())
# dp =[0 for _ in range(n + 1)]
# dp[0] = 1
# for i in range(1, n + 1):
#     for num in range(1, 5):
#         if i - num >= 0:
#             dp[i] += dp[i - num]
#
# print(dp[n])