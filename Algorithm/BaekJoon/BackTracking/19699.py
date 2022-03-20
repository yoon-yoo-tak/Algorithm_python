"""
19699 소-난다!

n개의 수중 m개의 합이 소수인것 만 출력

"""
import sys, math
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
ls = list(map(int, input().split()))
result = []
perm = permutations(ls, m)

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in perm:
    if is_prime_number(sum(i)):
        result.append(sum(i))

result = sorted(set(result))
if len(result)>0:
    print(" ".join(map(str, result)))
else:
    print(-1)