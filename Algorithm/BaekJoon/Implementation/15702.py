"""
15702 중간고사 채점
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
allot_points = list(map(int, input().split()))

examiners = []

for examiner_index in range(m):
    examiner_info = input().split()
    examiner_info[0] = int(examiner_info[0])
    examiner_score = 0
    for index in range(n):
        if examiner_info[index + 1] == 'O':
            examiner_score += allot_points[index]
    examiner_info.append(examiner_score)
    examiners.append(examiner_info)

examiners.sort(key=lambda x:(-x[-1], x[0]))

print(examiners[0][0], examiners[0][-1])