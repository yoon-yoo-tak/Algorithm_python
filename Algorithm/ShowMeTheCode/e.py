"""

"""
import sys
from itertools import permutations
input = sys.stdin.readline
n, k = map(int, input().split())
power = list(input().split())
people = list(map(int, input().split()))
total = sorted(zip(power, people))
perm = permutations(total, len(total))

ans = 0

for p in perm:
    temp = k
    temp_ans = 0
    prefix_sum = [[0] * 2 for _ in  range(n)]
    prefix_sum[0][0] = int(p[0][0])
    prefix_sum[0][1] = p[0][1]
    for i in range(1, n):
        prefix_sum[i][0] = prefix_sum[i - 1][0] * 2 + int(p[i][0])
        prefix_sum[i][1] = p[i][1]
    for pp, p in prefix_sum:
        temp -= pp
        if temp < 0:
            break
        temp_ans += p
    ans = max(ans, temp_ans)
print(ans)




