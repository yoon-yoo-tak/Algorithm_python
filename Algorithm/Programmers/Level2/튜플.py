"""
프로그래머스 2019 카카오 개발자 겨울 인턴십 - 튜플

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))