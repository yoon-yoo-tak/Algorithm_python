"""
단 한 번의 2048 시도
"""
import sys

input = sys.stdin.readline

mapping = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

board = [list(map(int, input().split())) for _ in range(4)]
direction = mapping[input().strip()]


