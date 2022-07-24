#  네이버 공채 2번

import sys
from collections import defaultdict

input = sys.stdin.readline
G, num_survey = map(int, input().split())
mem = defaultdict(dict)
for _ in range(num_survey):
    name, grade = input().split()
    if grade not in mem[name]:
        mem[name][grade] = 0
    mem[name][grade] += 1
ordered_mem = dict()
for name, survey_result in mem.items():
    arr = list(survey_result.items())
    arr.sort(key=lambda x: (-x[1], x[0]))
    ordered_mem[name] = [v[0] for v in arr]
grades = dict()
for i in range(G):
    grades[chr(i + ord('A'))] = []
for name, arr in ordered_mem.items():
    grades[arr[0]].append(name)


def compare(A, B):
    # 만약 A 가 B 보다 우선순위가 높다면 False, 아니면 True를 돌려주는 함수
    lenA = len(ordered_mem[A])
    lenB = len(ordered_mem[B])
    for i in range(max(lenA, lenB)):
        if i < lenA:
            vA = ordered_mem[A][i]
        else:
            vA = ordered_mem[A][0]

        if i < lenB:
            vB = ordered_mem[B][i]
        else:
            vB = ordered_mem[B][0]

        if vA < vB: return False
        if vA > vB: return True
    return A > B


for g, names in grades.items():
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if compare(names[i], names[j]):
                names[i], names[j] = names[j], names[i]
    if names:
        print(*names)
    else:
        print('-')
