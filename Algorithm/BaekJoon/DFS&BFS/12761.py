"""

12761 돌다리

"""
import sys
from collections import deque
input = sys.stdin.readline

a, b, n, m = map(int, input().split())

dist = [-1] * 100001

