"""
10974 모든순열

N까지의 수로 이루어진 모든 순열 출력

"""
import sys
from itertools import permutations

input = sys.stdin.readline


ls = [i for i in range(1, int(input())+1)]

for i in permutations(ls, len(ls)):
    print(" ".join(map(str, i)))
