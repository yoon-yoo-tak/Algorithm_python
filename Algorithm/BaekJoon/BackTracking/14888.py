"""
14888 연산자 끼워넣기
"""

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
min = 1e9
max = -1e9

def calc(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        if operand1 < 0:
            return -((-operand1) // operand2)
        else:
            return operand1 // operand2

def rec(k, value):
    if k == n - 1:
        global min, max
        min = min if min < value else value
        max = max if max > value else value
    else:
        global operators
        for cand in range(4):
            if operators[cand] >= 1:
                operators[cand] -= 1
                rec(k + 1, calc(value, cand, nums[k + 1]))
                operators[cand] += 1

rec(0, nums[0])
print(max)
print(min)