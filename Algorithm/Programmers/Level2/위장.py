"""
프로그래머스 위장

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

def solution(clothes):
    answer = 1
    temp = {}
    for i in clothes:
        if i[1] in temp:
            temp[i[1]] += 1
        else:
            temp[i[1]] = 1

    for i in temp.values():
        answer *= (i + 1)
    return answer - 1
