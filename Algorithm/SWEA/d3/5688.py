"""
5688 세제곱근을 찾아라

"""
import math

for tt in range(1, int(input()) + 1):
    num = int(input())
    triple = math.ceil(num ** (1/3))
    if triple ** 3 != num:
        print(f'#{tt} -1')
    else:
        print(f'#{tt} {triple}')