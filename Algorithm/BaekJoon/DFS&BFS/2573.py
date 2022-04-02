"""
2473 빙산

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def melt(x, y):
