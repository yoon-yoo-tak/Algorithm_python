"""

다트 게임

"""
import re

def solution(dartResult):
    pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    answer = []
    sol = {
        'S': lambda val: val,
        'D': lambda val: val ** 2,
        'T': lambda val: val ** 3
    }
    for num, cha, win in pattern.findall(dartResult):
        if cha == 'S':
            score = sol['S'](int(num))
        elif cha == 'D':
            score = sol['D'](int(num))
        elif cha == 'T':
            score = sol['T'](int(num))
        if win == '*':
            score *= 2
            if answer:
                answer[-1] *= 2
        elif win == '#':
            score *= -1
        answer.append(score)

    return sum(answer)


print(solution('1D2S0T'))