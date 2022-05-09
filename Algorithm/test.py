from itertools import permutations
import sys
input = sys.stdin.readline

t = int(input())

def check(q,w,e,r, aa):
    if aa[q] < aa[e] and aa[w] > aa[r]:
        return True
    return False

for _ in range(t):
    n = int(input())
    aa = list(map(int, input().split()))
    a, b, c, d = 0, a + 1, b + 1, c + 1

