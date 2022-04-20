import sys
from collections import deque
input = sys.stdin.readline

direction = [[],
             [[0], [1], [2], [3]],  # 1번 cctv
             [[0, 1], [2, 3]],      # 2번 cctv
             [[0, 2], [2, 1], [1, 3], [3, 0]],  # 3번 cctv
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]  # 4번 cctv
             ]

print(direction[1][0][0])