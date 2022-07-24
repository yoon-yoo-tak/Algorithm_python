"""
1644 소수의 연속합
"""
import sys

input = sys.stdin.readline
n = int(input())
prime = [True] * (n + 1)
prime[0] = prime[1] = False
nums = []
for i in range(2, n + 1):  # 에라모르겠다 췌
    if prime[i]:
        nums.append(i)
        for j in range(2 * i, n + 1, i):
            prime[j] = False

ans = total = r = 0

for l in range(len(nums)):  # 왼쪽
    while r < len(nums) and total < n: # 오른쪽, 합 조건
        total += nums[r]
        r += 1
    if total == n:
        ans += 1
    total -= nums[l]
print(ans)