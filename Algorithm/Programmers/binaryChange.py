"""
이진변환 반복하기

s에서 0 제거 > 길이를 2진법으로 표현
s가 1이 될 때까지 반복.
제거된 0갯수, 변환 횟수 출력

replace, count
"""

def solution(s):
    answer = []
    count = 0
    count_zero = 0
    while True:
        if s == '1':
            break
        count_zero += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        count += 1
    answer.append(count)
    answer.append(count_zero)
    return answer

print(solution("1111111"))
