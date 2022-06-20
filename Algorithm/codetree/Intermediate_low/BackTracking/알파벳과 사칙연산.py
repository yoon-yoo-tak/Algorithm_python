"""
알파벳과 사칙연산
1 ~ 4 중에 알파벳 갯수만큼 중복순열
"""
import sys

input = sys.stdin.readline

s = list(input().strip())
nums = [i for i in s if i.isalpha()]
operand = [i for i in s if i not in nums]
n = len(operand)
selected = []
ans = int(-1e11)
alpha = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5
}


def calc():
    equation = ''
    equation += '(' + str(selected[alpha[nums[0]]])
    for i in range(n):
        equation = '(' + equation + operand[i] + str(selected[alpha[nums[i + 1]]]) + ')'
    equation += ')'
    return equation

def rec(k):
    global ans
    if k == 6:
        ans = max(ans, eval(calc()))
        return
    else:
        for i in range(1, 5):
            selected.append(i)
            rec(k + 1)
            selected.pop()

rec(0)
print(ans)